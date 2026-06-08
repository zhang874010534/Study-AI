### ai学习

#### 大语言模型的基础单位Token

Token其实就是文本的片段，是大模型计算长度的单位，对于汉字，可以是字、词、甚至是半个字或者三分之一个字。

#### 预测token的机制

基于统计，通过大量数据的统计，找到下一个token

#### Agent

智能体指代具有自主性和智能的程序或系统，能够通过感知、规划、决策并执行相关任务

![image](./images/27636c00-59a8-4121-92d1-4e709e909ca0.png)

####  AI专有名词

- **LLM-大型语言模型**

  LLM是基于深度学习技术构建的人工智能模型，由具有数以亿计参数的人工神经网络组成，通过自监督学习或半监督学习在大量无标签文本上上进行训练。

- **AIGC-AI生成内容**

  AIGC（AI-Generated Content）通过对已有数据进行学习和模式识别，以适当的泛化能力生成相关内容的技术

- **AGI-人工通用智能**

  AGI (Artificial General Intelligence)全称人工通用智能，是指能够理解、学习和应用广泛的知识和技能的人工智能系统。

- **Agent-智能代理**

  Agent（智能代理）一个能够自主感知环境并采取行动的计算实体，其目标是最大化某种预定义的效用或实现特定的目标。

  AGI可以看成是一种非常高级的Agent，具备广泛适应性和

  自我学习能力，Agent也是现阶段AGI的最佳实现方式。

- **Prompt-提示词**

  Prompt是指给定的一段文本或问题，用于引导和启发人工智能模型生成相关的回答或内容。
  Prompt是目前人类与LLM大语言模型交互的核心方式。、

- **GPT-生成型预训练变换模型**

  GPT (Generative Pre-trained Transformer)是种基于深度学习的大型语言模型

  GPT模型最初由OpenAI开发，旨在通过训练模型预测下一个单词或字符来学习自然语言的统计规律。

- **Token-文本基础单元**

  Token是指在自然语言处理和文本处理任务中，将文本分解成较小单元的基本单位。这些单元可以是单词、字符、子词或其他语言单位，具体取决于任务和处理方式。

  大语言模型中的上下文长度计算一般都是基于Token，而不是字符，例如GPT-4的16K上下文意味着传递的消息不能超过16K个Token。

- **LoRA-插件式微调**

  LoRA (Low-Rank Adaptation of LLM)即插件式微调，用于对大语言模型进行个性化的特定任务的定制。

  LORA通过将模型的权重矩阵分解成低秩的相似矩阵，降低了参数空间的复杂性，从而减少微调的计算成本和模型存储要求。

- **矢量/向量数据库**

  矢量数据库是一种用于存储矢量/向量数据的数据库。
  矢量数据库可以存储和管理大量的矢量数据，例如图像、视频、音频、文本等，同时提供高效检索功能。

- **数据蒸馏**

  数据蒸馏指将给定的原始大数据集浓缩并生成一个小型数据，使得在小数据集上训练出来的模型与原数据集上训练的模型相似。
  数据蒸馏在深度学习领域被广泛应用，可以帮助将复杂的模型转换成更轻量级的模型，提高模型的鲁棒性和泛化能力。

#### LLM/RAG/Agent的技术路线

LLM/RAG/Agent已经成为人工智能领域进步的关键技术，理解这三者的概念与关系是做好面向AI编程开发的基础。

![image](./images/ad764e1e-8518-4d0b-ae64-7a3da80f7249.png)

#### AI Agent的定义与技术架构

![image-20260523100021530](./images/3a9c687d-e3e0-422b-a190-7debbf65333c.png)

#### 手动模拟Agent流程图

![img](./images/d3aa6f54-3e81-4f21-aa53-4dad2bd9f87f.png)

#### LLMOps项目需求拆分与设计

![d3aa6f54-3e81-4f21-aa53-4dad2bd9f87f](./images/c6017e1d-0c00-44b0-ad05-4e16a986df93.png)

#### 智能体、skills、工具、MCP

用户
 ↓
智能体：理解用户要什么
 ↓
Skills：判断这类任务应该怎么做
 ↓
工具：执行具体动作
 ↓
MCP：连接外部系统里的工具/数据

##### 智能体负责理解你要干嘛、判断要查什么、调用什么能力、最后组织回答。

##### Skills：更像“封装好的专项能力 / 使用说明书”  一个SOP

##### 工具：负责“干一个具体动作”  比如查订单工具 输入客户名，返回订单

##### MCP 是一种把外部工具接进来的协议

用户提问
 ↓
MaxKB 智能体理解：这是查销售数据
 ↓
发现 MCP 里有 query_database 工具
 ↓
调用 MCP Server：
{
  "tool": "query_database",
  "arguments": {
    "sql": "SELECT ..."
  }
}
 ↓
MCP Server 去数据库查询
 ↓
返回结果
 ↓
智能体组织成自然语言回答

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("order-mcp")

@mcp.tool()
def get_order(order_id: str) -> dict:
    """
    根据订单号查询订单信息
    """
    这里先写死，真实场景可以查数据库、调接口
    return {
        "order_id": order_id,
        "status": "已发货",
        "amount": 299,
        "customer": "张三"
    }

if __name__ == "__main__":
    mcp.run(transport="sse")
```

#### LLMOps项目7层架构

![01ac5c0cf09b783a26cbbccddd040ada](./images/01ac5c0cf09b783a26cbbccddd040ada.png)

#### 项目目录结构约定、规范与依赖注入

##### 项目结构

```js
---app // 应用入口集合
| ├---__init__.py
| └---http
|---config // 应用配置文件
| ├---__init__.py
| ├---config.py
| └---default_config.py
|---internal // 应用所有内部文件夹
| ├---core // LLM核心文件，集成LangChain、LLM、Embedding等非逻辑的代码
| | |---agent
| | |---chain
| | |---prompt
| | |---model_runtime
| | |---moderation
| | |---tool
| | |---vector_store
| | └---...
| ├---exception // 通用公共异常目录
| | ├---__init__.py
| | ├---exception.py
| | └---...
| ├---extension // Flask扩展文件目录
| | ├---__init__.py
| | ├---database_extension.py
| | └---...
| ├---handler // 路由处理器、控制器目录
| | ├---__init__.py
| | ├---account_handler.py
| | └---...
| ├---middleware // 应用中间件目录，包含校验是否登录
| | ├---__init__.py
| | └---middleware.py
| | └---...
| ├---migration // 数据库迁移文件目录，自动生成
| | ├---versions
| | └---...
| ├---model // 数据库模型文件目录
| | ├---__init__.py
| | ├---account.py
| | └---...
| ├---router // 应用路由文件夹
| | ├---__init__.py
| | ├---router.py
| | └---...
| ├---schedule // 调度任务、定时任务文件夹
| | ├---__init__.py
| | └---...
| ├---schema // 请求和响应的结构体
| | ├---__init__.py
| | └---...
| ├---server // 构建的应用，与app文件夹对应
| | ├---__init__.py
| | └---...
| ├---service // 服务层文件夹
| | ├---__init__.py
| | ├---oauth_service.py
| | └---...
| ├---task // 任务文件夹，支持即时任务+延迟任务
| | ├---__init__.py
| | └---...
|---pkg // 扩展包文件夹
| ├---__init__.py
| |---oauth
| | ├---__init__.py
| | ├---github_oauth.py
| | └---...
| └---... ├---storage // 本地存储文件夹
├---test // 测试目录
├---venv // 虚拟环境
├---.env // 应用配置文件
├---.gitignore // 配置git忽略文件
├---requirements.txt // 第三方包依赖管理
└---README.md // 项目说明文件
```

