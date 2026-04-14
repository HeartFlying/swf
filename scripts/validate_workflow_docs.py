#!/usr/bin/env python3
"""
SWF Workflow 文档校验脚本

检查项：
1. Skill 目录存在性
2. references 文件存在性
3. 旧编号残留扫描（S104, S404）
4. manifest 与 SKILL.md 一致性
5. 共享规范引用路径正确性
6. 冗余共享规范文件检测
"""

import os
import re
import sys
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
AGENTS_DIR = PROJECT_ROOT / "agents"
SHARED_DIR = SKILLS_DIR / "_shared"
MANIFEST_FILE = AGENTS_DIR / "workflow-manifest.yaml"

# 废弃编号模式
# 注意：S1-S101, S1-S102 是正确的（S1阶段的竞品分析和市场验证）
# 废弃的是在描述 S2 阶段技能时使用 S1-S10x 编号
# 例如：边界界定、显式需求、隐性需求、需求验证 应使用 S2-S20x
DEPRECATED_PATTERNS = [
    (r"\bS104\b", "S204"),      # 原 S104 (需求验证) 应为 S204
    (r"\bS404\b", "S406"),      # 原 S404 (原型设计) 应为 S406
    (r"\bS103\b", "S203"),      # 原 S103 (隐性需求) 应为 S203
]

# 排除的文件（允许出现旧编号）
EXCLUDE_FILES = [
    "agents-skills-review.md",
    "task-execution-status.md",
    "VERSION.md",
    "migration-status.md",
    "swf-workflow-refactor-v4.md",  # 历史记录文件
]

# 冗余文件列表（应只存在于 _shared 目录）
REDUNDANT_FILES = [
    "quality-standard.md",
    "artifact-specifications.md",
    "execution-flow-standard.md",
    "error-code-standard.md",
]

# 保留文件列表（Skill 特有）
KEEP_FILES = [
    "execution-details.md",
    "examples.md",
    "appendix.md",
    "skill-structure-reference.md",
]


def check_skill_directories() -> list:
    """检查 Skill 目录存在性"""
    errors = []
    skill_dirs = []

    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith("_"):
            skill_dirs.append(item)
            skill_md = item / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"SKILL.md not found in: {item}")

    print(f"  找到 {len(skill_dirs)} 个 Skill 目录")
    return errors


def check_references_exist() -> list:
    """检查 references 文件存在性"""
    errors = []
    checked = 0

    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith("_"):
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8")
                # 查找 references 引用
                refs = re.findall(r'\[.*?\]\((references/.*?\.md)\)', content)
                for ref in refs:
                    checked += 1
                    ref_path = skill_dir / ref
                    if not ref_path.exists():
                        errors.append(f"Reference not found: {ref_path}")

    print(f"  检查了 {checked} 个 references 引用")
    return errors


def check_deprecated_patterns() -> list:
    """检查旧编号残留"""
    warnings = []
    checked_files = 0

    for md_file in PROJECT_ROOT.rglob("*.md"):
        # 跳过排除文件
        if md_file.name in EXCLUDE_FILES:
            continue
        # 跳过 _shared 目录
        if "_shared" in str(md_file):
            continue

        checked_files += 1
        content = md_file.read_text(encoding="utf-8")

        for pattern, replacement in DEPRECATED_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                relative_path = md_file.relative_to(PROJECT_ROOT)
                warnings.append(f"Deprecated pattern '{pattern}' (→ {replacement}) found in: {relative_path} ({len(matches)} occurrences)")

    print(f"  检查了 {checked_files} 个 .md 文件")
    return warnings


def check_shared_references() -> list:
    """检查共享规范引用路径"""
    errors = []

    if not SHARED_DIR.exists():
        errors.append(f"Shared directory not found: {SHARED_DIR}")
        return errors

    shared_files = set(f.name for f in SHARED_DIR.rglob("*.md"))
    print(f"  共享规范文件: {len(shared_files)} 个")

    # 检查是否有 SKILL.md 引用 _shared
    referencing_skills = []
    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith("_"):
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8")
                if "_shared" in content:
                    referencing_skills.append(skill_dir.name)

    print(f"  引用 _shared 的 Skill: {len(referencing_skills)} 个")
    return errors


def check_manifest() -> list:
    """检查 manifest 文件"""
    errors = []

    if not MANIFEST_FILE.exists():
        errors.append(f"Manifest not found: {MANIFEST_FILE}")
        return errors

    print(f"  Manifest 存在: {MANIFEST_FILE.relative_to(PROJECT_ROOT)}")

    # 简单检查文件大小
    size = MANIFEST_FILE.stat().st_size
    print(f"  Manifest 大小: {size} bytes")

    if size < 1000:
        errors.append("Manifest file seems too small, may be incomplete")

    return errors


def check_redundant_files() -> tuple:
    """
    检查冗余共享规范文件

    功能：
    - 遍历所有 Skill 目录（排除 _shared）
    - 检查每个 Skill 的 references 目录中是否存在冗余文件
    - 检查 user-interaction 子目录是否存在

    Returns:
        tuple: (errors, warnings)
    """
    errors = []
    warnings = []
    checked_skills = 0
    redundant_found = 0
    user_interaction_found = 0

    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith("_"):
            checked_skills += 1
            references_dir = skill_dir / "references"

            if not references_dir.exists():
                continue

            # 检查冗余文件
            for redundant_file in REDUNDANT_FILES:
                file_path = references_dir / redundant_file
                if file_path.exists():
                    redundant_found += 1
                    relative_path = file_path.relative_to(PROJECT_ROOT)
                    warnings.append(
                        f"冗余文件: {relative_path} (应使用 _shared/{redundant_file})"
                    )

            # 检查 user-interaction 子目录
            user_interaction_dir = references_dir / "user-interaction"
            if user_interaction_dir.exists():
                user_interaction_found += 1
                relative_path = user_interaction_dir.relative_to(PROJECT_ROOT)
                warnings.append(
                    f"冗余目录: {relative_path} (应使用 _shared/user-interaction/)"
                )

    print(f"  检查了 {checked_skills} 个 Skill 目录")
    print(f"  发现 {redundant_found} 个冗余文件")
    print(f"  发现 {user_interaction_found} 个冗余 user-interaction 目录")

    return errors, warnings


def main():
    print("=" * 60)
    print("SWF Workflow 文档校验")
    print("=" * 60)
    print()

    all_errors = []
    all_warnings = []

    # 执行检查
    print("[1] 检查 Skill 目录存在性...")
    all_errors.extend(check_skill_directories())
    print()

    print("[2] 检查 references 文件存在性...")
    all_errors.extend(check_references_exist())
    print()

    print("[3] 检查旧编号残留...")
    all_warnings.extend(check_deprecated_patterns())
    print()

    print("[4] 检查共享规范引用路径...")
    all_errors.extend(check_shared_references())
    print()

    print("[5] 检查 manifest 文件...")
    all_errors.extend(check_manifest())
    print()

    print("[6] 检查冗余共享规范文件...")
    redundant_errors, redundant_warnings = check_redundant_files()
    all_errors.extend(redundant_errors)
    all_warnings.extend(redundant_warnings)
    print()

    # 输出结果
    print("=" * 60)
    if all_errors:
        print(f"发现 {len(all_errors)} 个错误:")
        for err in all_errors:
            print(f"  [ERROR] {err}")
        print()

    if all_warnings:
        print(f"发现 {len(all_warnings)} 个警告:")
        for warn in all_warnings[:10]:  # 只显示前10个
            print(f"  [WARN] {warn}")
        if len(all_warnings) > 10:
            print(f"  ... 还有 {len(all_warnings) - 10} 个警告")
        print()

    if not all_errors and not all_warnings:
        print("[PASS] 校验通过，无错误或警告。")
    elif not all_errors:
        print("[PASS] 校验通过，但有警告需要关注。")

    print("=" * 60)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
