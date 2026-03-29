# Coding Agent 集成优化路线图

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档版本 | v1.0.0 |
| 创建日期 | 2026-03-29 |
| 文档状态 | 待实施 |
| 关联版本 | swf-v3.2.0 |

---

## 一、背景与目标

### 1.1 背景

SWF (Software WorkFlow) 当前输出产物主要为 Markdown 文档格式，适合人类开发工程师阅读和参考。随着 AI 编程助手（Coding Agent）的普及，需要评估 SWF 产物作为 Coding Agent 输入的适配性。

### 1.2 目标

将 SWF 产出从"人类可读"升级为"机器可执行"，使 Coding Agent 能够：
1. 直接解析结构化产物
2. 自动生成代码骨架
3. 减少人工干预环节

### 1.3 评估结论摘要

| 维度 | 当前评分 | 目标评分 |
|------|---------|---------|
| 需求完整性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 架构可理解性 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 设计可执行性 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 产物可追溯性 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Coding Agent 就绪度 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 二、短期优化（P1 - 1-2 周期）

### 2.1 S5-A04 增强：OpenAPI 规范输出

**现状**：接口架构设计输出 Markdown 格式的 API 描述

**目标**：增加 OpenAPI 3.0 YAML 格式输出

**实施内容**：

1. 新增产物：`{PlanID}-S5-A04-002.yaml`

2. 输出格式示例：

```yaml
openapi: 3.0.3
info:
  title: {项目名称} API
  version: 1.0.0
  description: 由 SWF 自动生成

servers:
  - url: https://api.example.com/v1
    description: 生产环境

paths:
  /users:
    get:
      operationId: getUsers
      summary: 获取用户列表
      tags:
        - User
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: pageSize
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'

components:
  schemas:
    User:
      type: object
      required:
        - id
        - username
      properties:
        id:
          type: string
          format: uuid
        username:
          type: string
          maxLength: 50
        email:
          type: string
          format: email
        createdAt:
          type: string
          format: date-time

    UserListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        total:
          type: integer
        page:
          type: integer
        pageSize:
          type: integer
```

3. 修改文件：
   - `skills/s5-interface/SKILL.md` - 增加产物定义
   - `skills/s5-interface/template.yaml` - 新增 OpenAPI 模板
   - `skills/s5-interface/references/execution-details.md` - 增加生成逻辑

**验收标准**：
- [ ] OpenAPI YAML 可被 Swagger Editor 解析
- [ ] 支持生成 TypeScript Axios 客户端
- [ ] 支持生成 Java Spring 控制器骨架

---

### 2.2 S6-A01 增强：TypeScript Interface 输出

**现状**：模块详细设计输出 Mermaid 类图

**目标**：增加 TypeScript Interface 格式输出

**实施内容**：

1. 新增产物：`{PlanID}-S6-A01-002.ts`

2. 输出格式示例：

```typescript
/**
 * 自动生成于 SWF S6-A01
 * PlanID: P000001
 * 生成时间: 2026-03-29
 */

// ==================== 枚举定义 ====================

/**
 * 订单状态
 */
export enum OrderStatus {
  PENDING = 'PENDING',      // 待支付
  PAID = 'PAID',            // 已支付
  SHIPPED = 'SHIPPED',      // 已发货
  DELIVERED = 'DELIVERED',  // 已送达
  CANCELLED = 'CANCELLED'   // 已取消
}

// ==================== DTO 定义 ====================

/**
 * 创建订单请求
 */
export interface CreateOrderDTO {
  /** 收货地址ID */
  addressId: string;
  /** 商品列表 */
  items: OrderItemDTO[];
  /** 备注 */
  remark?: string;
}

/**
 * 订单项
 */
export interface OrderItemDTO {
  /** 商品ID */
  productId: string;
  /** 数量 */
  quantity: number;
  /** 单价 */
  price: number;
}

/**
 * 订单响应
 */
export interface OrderDTO {
  /** 订单ID */
  id: string;
  /** 订单号 */
  orderNo: string;
  /** 用户ID */
  userId: string;
  /** 订单状态 */
  status: OrderStatus;
  /** 总金额 */
  totalAmount: number;
  /** 创建时间 */
  createdAt: string;
  /** 更新时间 */
  updatedAt: string;
}

// ==================== 服务接口定义 ====================

/**
 * 订单服务接口
 */
export interface IOrderService {
  /**
   * 创建订单
   * @param dto 创建订单请求
   * @returns 订单信息
   * @throws {BusinessException} 商品库存不足
   * @throws {BusinessException} 地址不存在
   */
  createOrder(dto: CreateOrderDTO): Promise<OrderDTO>;

  /**
   * 取消订单
   * @param id 订单ID
   * @throws {BusinessException} 订单不存在
   * @throws {BusinessException} 订单已发货无法取消
   */
  cancelOrder(id: string): Promise<void>;

  /**
   * 获取订单详情
   * @param id 订单ID
   * @returns 订单信息
   */
  getOrderById(id: string): Promise<OrderDTO>;

  /**
   * 获取用户订单列表
   * @param userId 用户ID
   * @param page 页码
   * @param pageSize 每页数量
   * @returns 订单列表
   */
  getOrdersByUser(userId: string, page: number, pageSize: number): Promise<OrderDTO[]>;
}

// ==================== 异常定义 ====================

/**
 * 业务异常
 */
export interface BusinessException {
  /** 错误码 */
  code: string;
  /** 错误消息 */
  message: string;
  /** 错误详情 */
  details?: Record<string, unknown>;
}

/** 错误码常量 */
export const ErrorCodes = {
  ORDER_NOT_FOUND: 'ORDER_NOT_FOUND',
  ORDER_ALREADY_SHIPPED: 'ORDER_ALREADY_SHIPPED',
  INSUFFICIENT_STOCK: 'INSUFFICIENT_STOCK',
  ADDRESS_NOT_FOUND: 'ADDRESS_NOT_FOUND',
} as const;
```

3. 修改文件：
   - `skills/s6-module/SKILL.md` - 增加产物定义
   - `skills/s6-module/template.ts` - 新增 TypeScript 模板
   - `skills/s6-module/references/execution-details.md` - 增加生成逻辑

**验收标准**：
- [ ] TypeScript 编译通过（tsc --noEmit）
- [ ] 支持导出为 npm 包
- [ ] 包含完整的 JSDoc 注释

---

### 2.3 S6-A04 增强：测试代码骨架输出

**现状**：测试策略设计输出 Markdown 格式的测试文档

**目标**：增加 Jest 测试代码骨架输出

**实施内容**：

1. 新增产物：`{PlanID}-S6-A04-002.test.ts`

2. 输出格式示例：

```typescript
/**
 * 订单服务测试
 * 自动生成于 SWF S6-A04
 * PlanID: P000001
 */

import { describe, it, expect, beforeEach, jest } from '@jest/globals';

// ============================================
// 测试套件: OrderService
// ============================================

describe('OrderService', () => {
  let orderService: IOrderService;
  let mockOrderRepository: jest.Mocked<IOrderRepository>;
  let mockProductService: jest.Mocked<IProductService>;

  beforeEach(() => {
    // TODO: 初始化 mock 和 service
  });

  // ----------------------------------------
  // 测试用例: createOrder
  // ----------------------------------------

  describe('createOrder', () => {
    it('should create order successfully when all conditions are met', async () => {
      // Given: 用户已登录，购物车有商品，商品库存充足
      const dto: CreateOrderDTO = {
        addressId: 'addr-001',
        items: [
          { productId: 'prod-001', quantity: 2, price: 99.9 }
        ]
      };

      // When: 调用 createOrder
      const result = await orderService.createOrder(dto);

      // Then: 返回订单DTO，状态为 PENDING
      expect(result).toBeDefined();
      expect(result.status).toBe(OrderStatus.PENDING);
      expect(result.totalAmount).toBe(199.8);
    });

    it('should throw INSUFFICIENT_STOCK when product stock is not enough', async () => {
      // Given: 商品库存不足
      const dto: CreateOrderDTO = {
        addressId: 'addr-001',
        items: [
          { productId: 'prod-002', quantity: 100, price: 50 }
        ]
      };

      // When & Then: 抛出 INSUFFICIENT_STOCK 异常
      await expect(orderService.createOrder(dto))
        .rejects
        .toMatchObject({ code: ErrorCodes.INSUFFICIENT_STOCK });
    });

    it('should throw ADDRESS_NOT_FOUND when address does not exist', async () => {
      // Given: 地址不存在
      const dto: CreateOrderDTO = {
        addressId: 'non-existent',
        items: [
          { productId: 'prod-001', quantity: 1, price: 99.9 }
        ]
      };

      // When & Then: 抛出 ADDRESS_NOT_FOUND 异常
      await expect(orderService.createOrder(dto))
        .rejects
        .toMatchObject({ code: ErrorCodes.ADDRESS_NOT_FOUND });
    });
  });

  // ----------------------------------------
  // 测试用例: cancelOrder
  // ----------------------------------------

  describe('cancelOrder', () => {
    it('should cancel order successfully when order is pending', async () => {
      // Given: 订单存在且状态为 PENDING
      const orderId = 'order-001';

      // When: 调用 cancelOrder
      await orderService.cancelOrder(orderId);

      // Then: 订单状态变更为 CANCELLED
      const order = await orderService.getOrderById(orderId);
      expect(order.status).toBe(OrderStatus.CANCELLED);
    });

    it('should throw ORDER_ALREADY_SHIPPED when order is shipped', async () => {
      // Given: 订单已发货
      const orderId = 'order-002'; // 已发货订单

      // When & Then: 抛出 ORDER_ALREADY_SHIPPED 异常
      await expect(orderService.cancelOrder(orderId))
        .rejects
        .toMatchObject({ code: ErrorCodes.ORDER_ALREADY_SHIPPED });
    });

    it('should throw ORDER_NOT_FOUND when order does not exist', async () => {
      // Given: 订单不存在
      const orderId = 'non-existent';

      // When & Then: 抛出 ORDER_NOT_FOUND 异常
      await expect(orderService.cancelOrder(orderId))
        .rejects
        .toMatchObject({ code: ErrorCodes.ORDER_NOT_FOUND });
    });
  });
});

// ============================================
// 测试数据工厂
// ============================================

export class TestDataFactory {
  static createOrderDTO(overrides?: Partial<CreateOrderDTO>): CreateOrderDTO {
    return {
      addressId: 'addr-default',
      items: [{ productId: 'prod-default', quantity: 1, price: 100 }],
      ...overrides
    };
  }

  static createOrder(overrides?: Partial<OrderDTO>): OrderDTO {
    return {
      id: 'order-default',
      orderNo: 'ORD-001',
      userId: 'user-default',
      status: OrderStatus.PENDING,
      totalAmount: 100,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      ...overrides
    };
  }
}
```

3. 修改文件：
   - `skills/s6-test-strategy/SKILL.md` - 增加产物定义
   - `skills/s6-test-strategy/template.test.ts` - 新增测试模板
   - `skills/s6-test-strategy/references/execution-details.md` - 增加生成逻辑

**验收标准**：
- [ ] Jest 测试可执行（jest --passWithNoTests）
- [ ] Given-When-Then 结构与 S405 验收标准一致
- [ ] 包含异常分支测试用例

---

## 三、中期优化（P2 - 3-5 周期）

### 3.1 新增 Skill：S5-A07 项目脚手架设计

**目标**：输出项目初始化所需的所有配置文件

**新增产物**：

| 产物名称 | 文件格式 | 说明 |
|---------|---------|------|
| 目录结构定义 | `.tree` | 项目目录结构 |
| 依赖配置 | `package.json` | Node.js 项目依赖 |
| 构建配置 | `tsconfig.json` | TypeScript 配置 |
| 代码规范 | `.eslintrc.yaml` | ESLint 配置 |
| CI/CD 配置 | `.github/workflows/ci.yaml` | GitHub Actions 配置 |
| Docker 配置 | `Dockerfile` | 容器构建配置 |

**输出示例**：

```
# 项目目录结构
src/
├── api/                    # API 层
│   ├── controllers/        # 控制器
│   ├── middlewares/        # 中间件
│   └── routes/             # 路由定义
├── application/            # 应用层
│   ├── services/           # 业务服务
│   └── dtos/               # 数据传输对象
├── domain/                 # 领域层
│   ├── entities/           # 实体
│   ├── value-objects/      # 值对象
│   └── repositories/       # 仓储接口
├── infrastructure/         # 基础设施层
│   ├── database/           # 数据库实现
│   ├── external/           # 外部服务
│   └── repositories/       # 仓储实现
├── shared/                 # 共享模块
│   ├── common/             # 公共工具
│   └── config/             # 配置
└── main.ts                 # 入口文件
```

**验收标准**：
- [ ] npm install 无错误
- [ ] npm run build 编译通过
- [ ] Docker build 成功

---

### 3.2 新增 Skill：S6-A05 代码常量定义

**目标**：输出枚举类、常量、错误码定义

**新增产物**：

| 产物名称 | 文件格式 | 说明 |
|---------|---------|------|
| 枚举定义 | `enums.ts` | 所有枚举类型 |
| 常量定义 | `constants.ts` | 业务常量 |
| 错误码定义 | `error-codes.ts` | 错误码枚举 |
| 配置类型 | `config.ts` | 配置项类型定义 |

**输出示例**：

```typescript
// ==================== 业务状态枚举 ====================

/** 用户状态 */
export enum UserStatus {
  ACTIVE = 'ACTIVE',
  INACTIVE = 'INACTIVE',
  BANNED = 'BANNED',
}

/** 支付方式 */
export enum PaymentMethod {
  ALIPAY = 'ALIPAY',
  WECHAT = 'WECHAT',
  CREDIT_CARD = 'CREDIT_CARD',
  BANK_TRANSFER = 'BANK_TRANSFER',
}

// ==================== 业务常量 ====================

export const BusinessConstants = {
  /** 订单超时时间（分钟） */
  ORDER_TIMEOUT_MINUTES: 30,
  /** 最大重试次数 */
  MAX_RETRY_COUNT: 3,
  /** 默认分页大小 */
  DEFAULT_PAGE_SIZE: 20,
  /** 最大分页大小 */
  MAX_PAGE_SIZE: 100,
} as const;

// ==================== 错误码定义 ====================

export enum ErrorCode {
  // 通用错误 1xxx
  UNKNOWN_ERROR = 'E1000',
  INVALID_PARAMETER = 'E1001',
  UNAUTHORIZED = 'E1002',
  FORBIDDEN = 'E1003',
  NOT_FOUND = 'E1004',

  // 用户相关 2xxx
  USER_NOT_FOUND = 'E2001',
  USER_ALREADY_EXISTS = 'E2002',
  INVALID_PASSWORD = 'E2003',

  // 订单相关 3xxx
  ORDER_NOT_FOUND = 'E3001',
  ORDER_ALREADY_CANCELLED = 'E3002',
  ORDER_ALREADY_PAID = 'E3003',
  INSUFFICIENT_STOCK = 'E3004',

  // 支付相关 4xxx
  PAYMENT_FAILED = 'E4001',
  PAYMENT_TIMEOUT = 'E4002',
}

/** 错误码映射 */
export const ErrorMessages: Record<ErrorCode, string> = {
  [ErrorCode.UNKNOWN_ERROR]: '未知错误',
  [ErrorCode.INVALID_PARAMETER]: '参数错误',
  [ErrorCode.UNAUTHORIZED]: '未授权',
  [ErrorCode.FORBIDDEN]: '禁止访问',
  [ErrorCode.NOT_FOUND]: '资源不存在',
  [ErrorCode.USER_NOT_FOUND]: '用户不存在',
  [ErrorCode.USER_ALREADY_EXISTS]: '用户已存在',
  [ErrorCode.INVALID_PASSWORD]: '密码错误',
  [ErrorCode.ORDER_NOT_FOUND]: '订单不存在',
  [ErrorCode.ORDER_ALREADY_CANCELLED]: '订单已取消',
  [ErrorCode.ORDER_ALREADY_PAID]: '订单已支付',
  [ErrorCode.INSUFFICIENT_STOCK]: '库存不足',
  [ErrorCode.PAYMENT_FAILED]: '支付失败',
  [ErrorCode.PAYMENT_TIMEOUT]: '支付超时',
};
```

**验收标准**：
- [ ] 无重复枚举值
- [ ] 错误码与 S6-A04 测试用例一致
- [ ] 支持多语言扩展

---

## 四、长期优化（P3 - 6+ 周期）

### 4.1 结构化产物格式标准化

**目标**：所有关键产物同时输出 YAML/JSON 格式

**实施方案**：

1. 定义 SWF 产物 Schema
2. 为每个 Skill 增加结构化输出模板
3. 提供产物验证工具

**Schema 示例**：

```yaml
# swf-artifact-schema.yaml
$schema: http://json-schema.org/draft-07/schema#
type: object
required:
  - meta
  - content
properties:
  meta:
    type: object
    required:
      - planId
      - skillId
      - artifactId
      - version
      - generatedAt
    properties:
      planId:
        type: string
        pattern: "^P[0-9]{6}$"
      skillId:
        type: string
        pattern: "^S[0-9]-[A-Z0-9]+$"
      artifactId:
        type: string
      version:
        type: string
        pattern: "^v[0-9]+\\.[0-9]+\\.[0-9]+$"
      generatedAt:
        type: string
        format: date-time
```

---

### 4.2 代码生成模板系统

**目标**：支持多语言代码生成

**实施方案**：

1. 引入 Handlebars/Mustache 模板引擎
2. 定义通用数据模型
3. 提供多语言模板库

**模板示例**：

```handlebars
// service.ts.hbs
import { Injectable } from '@nestjs/common';
import { {{interfaceName}} } from './{{interfaceName}}';
{{#each imports}}
import { {{name}} } from '{{path}}';
{{/each}}

@Injectable()
export class {{className}} implements {{interfaceName}} {
  {{#each dependencies}}
  private readonly {{name}}: {{type}};
  {{/each}}

  constructor(
    {{#each dependencies}}
    {{name}}: {{type}}{{#unless @last}},{{/unless}}
    {{/each}}
  ) {
    {{#each dependencies}}
    this.{{name}} = {{name}};
    {{/each}}
  }

  {{#each methods}}
  async {{name}}({{#each parameters}}{{name}}: {{type}}{{#unless @last}}, {{/unless}}{{/each}}): Promise<{{returnType}}> {
    // TODO: 实现逻辑
    throw new Error('Not implemented');
  }
  {{/each}}
}
```

---

### 4.3 双向追溯系统

**目标**：需求 ID → 代码文件的完整映射

**实施方案**：

1. 在代码注释中嵌入需求 ID
2. 构建追溯索引文件
3. 支持影响分析查询

**追溯索引示例**：

```yaml
# traceability-index.yaml
requirements:
  R001:
    description: 用户注册
    stories: [US001, US002]
    modules: [UserService, UserController]
    tests: [user.service.test.ts]
    files:
      - src/application/services/user.service.ts
      - src/api/controllers/user.controller.ts
      - src/domain/entities/user.ts

  R002:
    description: 用户登录
    stories: [US003]
    modules: [AuthService, AuthController]
    tests: [auth.service.test.ts]
    files:
      - src/application/services/auth.service.ts
      - src/api/controllers/auth.controller.ts
```

---

## 五、实施优先级矩阵

| 优化项 | 价值 | 工作量 | 优先级 | 预计周期 |
|--------|------|--------|--------|---------|
| S5-A04 OpenAPI 输出 | 高 | 低 | P1 | 1 周期 |
| S6-A01 TypeScript 输出 | 高 | 中 | P1 | 2 周期 |
| S6-A04 测试骨架输出 | 高 | 中 | P1 | 2 周期 |
| S5-A07 项目脚手架 | 中 | 高 | P2 | 3 周期 |
| S6-A05 常量定义 | 中 | 低 | P2 | 1 周期 |
| 结构化产物格式 | 中 | 高 | P3 | 4 周期 |
| 代码生成模板系统 | 高 | 高 | P3 | 6 周期 |
| 双向追溯系统 | 低 | 高 | P3 | 4 周期 |

---

## 六、验收检查清单

### 6.1 Coding Agent 就绪度评估

完成以下检查后，可认为 SWF 产物已适配 Coding Agent：

**基础能力**：
- [ ] OpenAPI YAML 可被 Swagger 解析
- [ ] TypeScript Interface 编译通过
- [ ] DDL 脚本可执行
- [ ] 测试骨架可运行

**进阶能力**：
- [ ] 可自动生成项目脚手架
- [ ] 可自动生成 CRUD 代码
- [ ] 可自动生成测试用例

**高级能力**：
- [ ] 支持多语言代码生成
- [ ] 支持需求-代码双向追溯
- [ ] 支持增量更新代码

---

## 七、版本规划

| 版本 | 发布内容 | 预计时间 |
|------|---------|---------|
| v3.3.0 | P1 短期优化（OpenAPI + TypeScript + 测试骨架） | Q2 2026 |
| v3.4.0 | P2 中期优化（脚手架 + 常量定义） | Q3 2026 |
| v4.0.0 | P3 长期优化（结构化产物 + 模板系统 + 追溯系统） | Q4 2026 |

---

## 八、参考资料

- [OpenAPI Specification 3.0](https://swagger.io/specification/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [ISO/IEC 25010 Quality Model](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)

---

*文档创建于 2026-03-29，待项目实施后对标优化*
