# 留声：每日灵感

> 配套文档：[留声](voice-legacy.md) · [类似项目调研](voice-legacy-research.md)
> Claude 每天到网上转一圈，把找到的灵感记在这里。最新的在最上面。

<!-- 新条目插入在这一行下面 -->

## 2026-10-16 · 技术细节

### 发现
- **Infura 关停 IPFS 服务**：Infura 在 2026 年 8 月 3 日停止新上传和固定（pin），8 月 15 日关闭 IPFS API 和专用网关；内容的 CID 不变，但所有写死了 Infura 地址的应用要自己改。留声的"日常存储"如果依赖某家托管 pin 服务，就会遇到同样的事。具体关停后的现状未逐条确认。[Filecoin 博客](https://filecoin.io/blog/Infuras-IPFS-Service-is-Shutting-Down-August-15-2026) · [Filebase 迁移指南](https://filebase.com/blog/infura-ipfs-is-shutting-down-how-to-migrate/)
- **Arweave 的"永久"是怎么算出来的**：一次付费，大部分进入"捐赠基金"，再慢慢付给矿工；定价按约 200 年的存储成本计算，前提是存储成本每年至少下降 0.5%，降得更快则存得更久。所以"永久"是一个经济假设，不是物理保证，而且付费是用 AR 币计价，法币价格会随币价大幅波动（ArDrive 文章里出现过每 GB 3–8 美元和 30–45 美元两种量级，文章未标日期）。可以直接补充 voice-legacy.md 里"每 GB 约 10 美元"的粗算的不确定性。[Arweave 存储基金解释](https://permaweb-journal.ar.io/reference/storage-endowment.html) · [ArDrive](https://ardrive.io/?p=744)
- **美国国会图书馆偏好无损的 Broadcast WAVE**：馆里对音频的首选归档格式是封装 LPCM 的 Broadcast WAVE；我没能确认它对 Opus / FLAC 的态度（页面抓取失败，现状未确认）。这和留声草案里"Opus 一小时约 10MB"的体积估算有一个需要意识到的差别：机构做长期保存时偏向无损，体积大得多。[LoC 格式说明](https://www.loc.gov/preservation/digital/formats/fdd/fdd000357.shtml)
- **档案界的做法：校验和 + 定期巡检 + 多地副本**：NDSA 的指引强调，只记录指纹不够，要按计划定期核对，发现损坏能用另一份副本修复；存储层级从"两份不在同一处"到"三份以上、处在不同灾害风险的地点"。格式过时是另一个独立问题，指纹管不了。[NDSA Fixity 指南](https://www.digitalpreservation.gov/ndsa/working_groups/documents/NDSA-Fixity-Guidance-Report-final100214.pdf)
- **互联网档案馆、史密森尼已把音频放上 Filecoin / IPFS**：公共领域有声书、Bell 的数字化录音等。说明机构层面的"去中心化保存"已有先例，可以作为将来"交给公共机构兜底"的参照。[Internet Archive 博客](https://blog.archive.org/tag/filecoin/)

### 今天的一个想法
**钥匙卡 / 寻回线索里写"内容指纹"，不写"网址"。** Infura 的例子说明，服务会关，地址会失效，只有按内容寻址的 CID 不变。托付模式生成的钥匙（或"陶瓷小牌"式的短码）可以包含：录音的内容哈希 + 解锁日期 + 一句"用任何 IPFS / Arweave 工具按这个哈希去找"，不绑定任何一家网关或 pin 服务。再配合档案界的"定期巡检"：志愿者节点定期核对每段录音的哈希，坏了从别的副本修复，这样"像做种一样"的社区存储才有说得出口的可靠性。这些都不改变已定的立场，只是让寻回不依赖留声自己活着。

### 可以继续挖
- LoC 对 Opus / FLAC 的明确态度，以及"原样"录下来的 Opus 码流，是否需要同时在手机本地留一份无损（只是技术核实，不是改立场）
- IPFS Cluster / Kubo 志愿者节点的实际巡检、自动修复机制，和 Arweave 当前实时报价接口（gateway 的 price endpoint）

