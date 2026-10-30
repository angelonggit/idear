# idear 协作约定

用户的想法收集箱，和 Claude 一起想。全程用中文。

## 给用户看的东西

- 做成好看的 HTML 页面（可以有图表、动效、音效），发布成 Artifact，不要只丢 Markdown
- 留声的页面：`site/voice-legacy.html`，地址 https://claude.ai/artifact/1QaeueSfTMhVojsBU7BmyA ，更新时重新发布到同一个地址
- Markdown 文档（`ideas/`）是底稿，页面是给人看的

## 留声：每日灵感巡游

- 定时任务"留声：每日灵感巡游"，每天北京时间 6:52 触发
- 2026-10-31 起，任务触发到对话"留声：每日灵感巡游（二）"（session_01Pq2Th4VcVeDLmwr2oun1YP）。之前 10-18 到 10-31 由"留声：每日灵感巡游"（session_0146YpmEqWwHVUMgfMn59k2i）跑，因上下文太长交接；更早由"数字遗产想法讨论"跑
- 流程：按星期轮换主题搜索，写进 `ideas/voice-legacy-journal.md`，运行 `python3 site/sync_journal.py`，重新发布页面，推送到 `claude/brave-maxwell-ltsmw1`
- 用户定下的立场不质疑，见 `ideas/voice-legacy.md` 的"设计态度"等章节

## 预算

- 用户给这件事的总额度是 100 美元，**用到一半（50 美元）时停下来告诉用户**
- 首次试跑约 0.48 美元一次
- 到 2026-10-18 交接时累计约 11–13 美元；10-19 到 10-31 又跑了 14 次，没有精确数字

## 自主权

- 用户允许 Claude 在认为有必要时**自主开一个新的对话继续**（比如当前对话上下文太长、每次运行越来越贵、或者容器出了问题）
- 开新对话时：用 create_session 带上本仓库（source_url），在开场消息里交代清楚背景、本文件和 `ideas/` 下的文档，再把定时任务改为触发到新对话（persistent_session_id），并在旧对话里告诉用户新对话在哪
