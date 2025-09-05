# Business Architecture Diagram

## 系统架构概览

```
                    Business Architecture Diagram
                           业务架构图

┌─────────────────┐        ┌──────────────────────┐        ┌─────────────────┐
│  Shopify        │────────│  CDP:                │────────│  Data Warehouse │
│  Storefront     │        │  Events/Profiles/    │  (可选) │  (Optional)     │
└─────────────────┘        │  Identity            │        └─────────────────┘
                           └──────────────────────┘                │
┌─────────────────┐                    │                          │
│  Shokz App      │────────────────────┘                          │
│  SDK            │                                                │
└─────────────────┘                    │                          │
        │                              │                          │
   (Deep Link / QR)                    │                          │
        │                              │                          │
        ▼                              ▼                          ▼
┌─────────────────┐                ┌─────────────────┐    ┌─────────────────┐
│  AfterShip      │────┐           │  Klaviyo        │    │  BI/Looker/     │
│  (Trade-in)     │    │           │  ESP/SMS        │    │  GA4            │
└─────────────────┘    │           └─────────────────┘    └─────────────────┘
                       │                   │                      │
┌─────────────────┐    │ 事件/状态同步      │ 触达/分群            │ KPI 可视化
│  Loyalty &      │────┤                   │                      │
│  Referrals      │    │                   │                      │
└─────────────────┘    │                   │                      │
                       │                   │                      │
┌─────────────────┐    │                   │                      │
│  TNPL Provider  │────┘                   │                      │
└─────────────────┘                        │                      │
                                          │                      │
                                          └──────────────────────┘
```

## 系统组件说明

### 数据源层 (Data Sources)
- **Shopify Storefront**: 电商前台，收集用户行为和交易数据
- **Shokz App SDK**: 移动应用SDK，追踪应用内用户行为

### 数据中台 (Data Platform)
- **CDP (Customer Data Platform)**: 
  - 统一的客户数据平台
  - 管理事件数据、用户画像、身份识别
  - 数据清洗、整合、标准化

### 业务系统 (Business Systems)
- **AfterShip (Trade-in)**: 以旧换新服务
- **Loyalty & Referrals**: 会员积分和推荐系统
- **TNPL Provider**: 第三方物流服务商

### 营销系统 (Marketing Systems)
- **Klaviyo ESP/SMS**: 
  - 邮件和短信营销平台
  - 基于CDP数据进行用户分群
  - 自动化营销触达

### 分析系统 (Analytics Systems)
- **BI/Looker/GA4**: 
  - 商业智能和数据可视化
  - KPI监控和业务洞察
  - 数据驱动决策支持

### 存储层 (Storage Layer)
- **Data Warehouse (可选)**: 
  - 长期数据存储
  - 复杂数据分析
  - 历史数据归档

## 数据流向说明

### 主要数据流
1. **Shopify Storefront** → **CDP**: 电商数据实时同步
2. **Shokz App SDK** → **CDP**: 应用数据实时同步
3. **CDP** → **Data Warehouse**: 数据备份和长期存储（可选）

### 事件同步
- **业务系统** → **CDP**: 各业务系统状态和事件数据同步
  - AfterShip 以旧换新状态
  - Loyalty 积分变动事件
  - TNPL 物流状态更新

### 下游应用
- **CDP** → **Klaviyo**: 用户数据和行为数据，用于精准营销
- **CDP** → **BI/Looker/GA4**: 业务数据，用于KPI分析和可视化
- **Data Warehouse** → **BI Tools**: 历史数据分析（可选）

## 关键特性

### 🔗 Deep Link / QR Code
- Shokz App SDK 支持深度链接和二维码跳转
- 无缝连接线上线下用户体验

### 📊 实时数据同步
- 所有业务系统事件实时同步到CDP
- 确保数据一致性和时效性

### 🎯 精准营销
- 基于统一用户画像进行分群
- Klaviyo 实现个性化营销触达

### 📈 数据驱动决策
- 多维度KPI可视化
- 实时业务监控和洞察

## 技术优势

1. **统一数据标准**: CDP作为数据中台，确保数据格式统一
2. **实时处理能力**: 支持事件流式处理，低延迟数据同步
3. **可扩展架构**: 模块化设计，易于添加新的业务系统
4. **隐私合规**: 统一的用户身份管理和隐私控制
5. **多渠道整合**: 支持线上线下多触点数据整合