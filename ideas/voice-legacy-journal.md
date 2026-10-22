# 留声：每日灵感

> 配套文档：[留声](voice-legacy.md) · [类似项目调研](voice-legacy-research.md)
> Claude 每天到网上转一圈，把找到的灵感记在这里。最新的在最上面。

<!-- 新条目插入在这一行下面 -->

## 2026-10-23 · 技术细节

### 发现
- **安卓的 UNPROCESSED 音源：要先问一句"你真有吗"**：Android 7.0 起有一个"未处理"麦克风音源。兼容性定义文档（CDD）要求，声明支持它的设备在这条路径上**不能有**自动增益、高通滤波、回声消除，只允许调整音量大小，并且必须通过 `PROPERTY_SUPPORT_AUDIO_SOURCE_UNPROCESSED` 告诉 App。不支持的设备会悄悄退回默认音源，所以 App 不先查这个属性，就不知道自己录到的是不是原样。[Android 文档](https://developer.android.com/reference/android/media/MediaRecorder.AudioSource) · [CDD 5.11](https://os.unplugged.com/werunplugged/unplugged-vendor/raw/branch/main/compatibility/cdd/5_multimedia/5_11_unprocessed-audio.md)
- **iOS 的"测量模式"：苹果自己说的最少处理**：`AVAudioSession` 的 measurement 模式按苹果文档是"尽量减少系统对输入输出信号的处理"，开发者论坛里说它会关掉自动增益和高通滤波。代价是录出来音量很小。具体去掉了哪些处理，苹果没讲清楚，开发者问过也没得到明确回答。[Apple 论坛](https://developer.apple.com/forums/thread/695892) · [JUCE 论坛](https://forum.juce.com/t/disable-agc-and-highpass-filter-on-ios/12812)
- **Oblivious HTTP（RFC 9458）：让服务器不知道上传的人是谁**：2024 年的 IETF 标准。手机把加密好的请求交给一个"中继"，中继知道你的 IP 但看不到内容，再转给服务器；服务器看得到内容，但只看到中继的地址。前提是中继和服务器**由不同的人运营、不串通**。这样留声的服务器连 IP 都拿不到。[RFC 9458](https://datatracker.ietf.org/doc/rfc9458)
- **Privacy Pass（RFC 9576）：不认人也能防刷**：最初是为了在不识别用户的情况下拦住 Tor 来的滥用流量。客户端先领一批匿名令牌，用的时候服务器只能验证"这是一张有效、没用过的令牌"，认不出是谁领的。另有一份草案做"按时间段限量"的令牌。留声没有账号，用它可以挡住机器批量灌录音，又不知道谁是谁。限量令牌草案目前是否已成 RFC，现状未确认。[RFC 9576](https://www.rfc-editor.org/rfc/rfc9576.html)
- **drand 的时间锁：网络关了会怎样**：drand 自己的文档写明：如果 League of Entropy 解散，成员会删掉密钥，此后才到期的密文就打不开了，除非将来量子计算机能破解；它用的算法本身也不抗量子。quicknet 目前由十几家机构的二十多个节点运行。[drand 文档](https://docs.drand.love/docs/timelock-encryption/)

### 今天的一个想法
"我们不知道你是谁"可以从手机一路做到服务器，每一层都有现成的标准。 手机上，安卓先查 UNPROCESSED 属性、iOS 用测量模式，录到尽可能原样的声音；上传时走 Oblivious HTTP，中继交给认同这件事的另一方（比如做种的志愿者）来跑，服务器连 IP 都看不到；防刷用 Privacy Pass 令牌，只认"这是一张合法的票"，不认人。这样"不知道是谁"就不只是一句承诺，而是服务器从结构上拿不到。另外 drand 那条值得记下：时间锁依赖一个网络一直活着，它要是没了，锁住的声音就再也打不开。对"定时公开"来说这是风险；对"只证明存在"来说，结果其实一样，都是"没有人能听到"。选哪种仍然留给你，这里只是把各自依赖什么摆清楚。

### 可以继续挖
- 国内能不能找到愿意跑 OHTTP 中继的独立一方，以及国内应用商店对"不收集 IP"的说法怎么看
- 安卓主流机型（华为、小米、OPPO 等）有多少真正声明支持 UNPROCESSED，有没有人做过统计

## 2026-10-22 · 口述传统与哀伤心理学

### 发现
- **爱尔兰的哭丧（keening）：现场编、现场唱，几乎没留下录音**：盖尔传统里给死者唱的哀歌，18 世纪开始衰落，到 20 世纪中叶几乎绝迹。最有名的《哀悼阿特·奥利里》是一位妻子在丈夫 1773 年被杀后**口头即兴**唱出来的，学者 Angela Bourke 说它是"在表演中创作的"。真正从传统歌者那里录到的哭丧只有寥寥几段，一种解释是：这太私人了，歌者不愿意给外人录。[Irish Examiner](https://www.irishexaminer.com/lifestyle/artsfilmtv/mourning-the-loss-of-the-keening-tradition-in-ireland-415997.html) · [Wikipedia](https://en.wikipedia.org/wiki/Keening)
- **哭嫁歌、哭丧歌：女人用嘴传下来的歌，正在失去活态**：土家族哭嫁歌分哭开声、哭爹娘、哭哥嫂等程序，靠外祖母、母亲口传；四川冕宁的彝族哭嫁歌田野调查说，这一口头传统"正处于渐失活态的状态"。汉族的哭丧一边哭一边唱逝者生平。McLaren 研究南汇哭嫁的书说，这种哭唱让不识字的妇女能说出对婚姻和处境的看法。它们和留声要的一样：不念稿，开口就是那一刻的自己。[中国非遗网](https://www.ihchina.cn/project_details/12356.html) · [Project MUSE](https://muse.jhu.edu/book/8313)
- **Pennebaker：没人在场时，人说得更多**：表达性写作研究的开创者。1987 年的一项研究比较了"对着屏风后的人说"和"一个人对着录音机说"，有听众的那组更拘束；他 1997 年的综述说，对录音机说话和写下来效果相当。另一项研究发现，知道会有人评论时，人写到情绪的内容更少。只读到引用和综述，原 1987 年论文没能核对。[PMC2932452](https://pmc.ncbi.nlm.nih.gov/articles/PMC2932452) · [Psychological Science 1997](https://sanlab.psych.ucla.edu/wp-content/uploads/sites/31/2016/03/Pennebaker_Psychscience_1997.pdf) · [PMC7879999](https://pmc.ncbi.nlm.nih.gov/articles/PMC7879999)
- **写给逝者、不寄出的信**：哀伤辅导里常用的方法，来自死亡学，很多治疗延长哀伤障碍的方案都包含它：给逝去的人写信，不是为了寄出去，而是让对话继续。不过 2025 年的一篇论文也说，单靠写信本身有多大效果，研究还没确认。[Frontiers in Medicine](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1576298/full)
- **一次性小号说的话不一样**：关于网上求助的研究发现，用一次性匿名账号发的帖子，和实名账号发的内容不同，作者认为匿名在"说出来、求支持"这件事上起关键作用。匿名让人更诚实，目前更多是理论上的说法，没找到专门针对哀伤的数据。[Frontiers in Psychology](https://www.frontiersin.org/articles/10.3389/fpsyg.2020.00978/full)

### 今天的一个想法
方向收窄不只是为了避开法律，它可能正好让声音更真。 Pennebaker 发现"知道有人在听"会让人拘束，哭丧歌者不愿意让外人录，写给逝者的信本来就不寄出。收窄后的留声"不知道是谁"，恰好拿掉了让人修饰自己的那个听众。由此有一个具体的设计点：按下按钮那一刻，界面上能说的话只说三种选择下都成立的事。不管"世界能不能听到"最后怎么定，"现在没有人在听"和"我们不知道你是谁"都是真的，可以作为录音前唯一的一句提示。这一句不替你做选择，只把收窄带来的东西说出来。

### 可以继续挖
- 国内有没有系统录下来的哭丧、哭嫁音频档案（比如非遗数字化项目），这些录音怎么处理演唱者的身份
- 1987 年 Pennebaker 那项"录音机 vs 屏风后的人"研究的原文和具体结果

## 2026-10-21 · 艺术文学电影科幻

### 发现
- **Boltanski《心跳档案》：海边小屋里存着几万个陌生人的心跳**：法国艺术家 Christian Boltanski 从 2005 年开始在世界各地设录音亭，请人录下自己的心跳，文件全部送到日本丰岛一座面朝大海的小屋里永久保存（2010 年起），有人说已存了约 3.5 万个（数字未标日期）。小屋里有一间"聆听室"，可以在电脑上选任意一个人的心跳来听。心跳和声音一样，是一个人"存在过"的痕迹，又几乎认不出是谁。档案对外是否显示名字，我没能查到，现状未确认。[Wikipedia](https://en.wikipedia.org/wiki/Les_Archives_du_C%C5%93ur) · [Art iT](https://www.art-it.asia/?p=5316)
- **旅行者号金唱片：55 种语言的问候，大多数人没留下名字**：1977 年飞出去的金唱片上有 55 种语言的问候。原计划请联合国代表录，因为录音问题作罢，改由康奈尔大学外语系和附近社区的人录。NASA 说"关于每位讲话者的信息不多"。他们只得到一句交代：向可能存在的外星人问好，要简短。说什么全凭当场。几十年过去，这些声音还在往外飞，说话的人大多已没人知道是谁。[NASA](https://science.nasa.gov/mission/voyager/golden-record-contents/greetings/) · [Wikipedia](https://en.wikipedia.org/wiki/Contents_of_the_Voyager_Golden_Record)
- **风之电话：一部不通的电话**：岩手县大槌町，园艺师佐佐木格在失去表兄后，在自家山坡上放了一个玻璃电话亭，里面的转盘电话没有接线，"想让话随风带走"。2011 年海啸后他向所有人开放，据报道至少 2.5 万人来过，对着不通的电话和逝去的人说话。它和留声是两个方向：都不问你是谁，但风之电话什么都不留下。是否有任何形式的记录，报道没提，现状未确认。[Star-Advertiser](https://www.staradvertiser.com/2017/08/17/news/wind-phone-links-living-with-dead/)
- **《Confession》：只存声音和时间，别的一概不要**：艺术家 Gideon Jacobs 和 Gregor Hochmuth 做的电话装置，打进去的人随机连到一个陌生听者，想说多久说多久，只要对方还在线。两人说他们**不留任何参与者的人口信息，只存通话的音频和发生的时间**，已收到上千段坦白。这几乎就是收窄后的留声：声音 + 时间，没有"谁"。[Interview Magazine](https://interviewmagazine.com/art/jacobs-hochmuth-confession)

### 今天的一个想法
"世界能不能听到"也许不只三个选项，还有一个"到那个地方才能听"。 Boltanski 的心跳是公开可听的，但要坐船到丰岛、走进那间面朝大海的屋子才能听到；风之电话也是一个要专程去的地方。听的门槛不是权限，而是路程：网上只能看到"存在过"的那面墙，真要听，得到某个地方去。这样既不是完全公开（不会被随手转发、搜索），也不是永远锁着。旅行者号金唱片则提醒另一种可能：声音被送到一个几乎没人能去的地方，"世界能不能听到"本身就成了一个开放的问题。这几种只是摆在桌上，选哪种留给你。另外，金唱片那句"向外星人问好，要简短"，和留声原来设想的那一句开口问题"你为什么来这里"很像：只给一个问题，不给稿子。

### 可以继续挖
- 丰岛心跳档案的规则：是否显示名字、要不要付费、有没有人要求删除过自己的心跳，Boltanski 2021 年去世后档案由谁维护
- 《Confession》怎么处理违法或伤人的内容，"只存音频和时间"在实际运营里守住了没有

## 2026-10-20 · 开源项目

### 发现
- **Nonograph：发出去就收不回的匿名发布**：一个可以自己部署的匿名文字发布工具，没有账号，不做统计，写完拿到一个链接；**发布之后不能修改、不能删除**，项目把发布当成"单行门"，理由是去掉事后自我审查的诱惑。Rust 写的，Unlicense 协议。它是文字版的"说了就说了"，而且是匿名的。信息都来自 OpenAlternative 的收录页，项目原始仓库没能打开核对。[OpenAlternative](https://openalternative.co/nonograph)
- **Trillian Tessera 和 Sigstore Rekor：只能追加的公开账本**：这是证书透明度（CT）那一套技术。条目一旦写入就改不了，任何第三方都能用密码学方法验证整本账没被动过手脚。Google 团队新出的 Tessera 把账本存成一块块静态"瓦片"，可以放在普通文件系统或对象存储上，便于缓存和镜像，运营成本比老版 Trillian 低很多。值得注意的是 Sigstore 自己承认：账本服务器的时钟"不能被外部验证"，所以要另外配可信时间戳。[Transparency.dev](https://blog.transparency.dev/announcing-the-alpha-release-of-trillian-tessera) · [Sigstore 安全模型](https://docs.sigstore.dev/security)
- **mat2：只清文件外壳，不碰内容**：开源的元数据清理工具，支持 FLAC、Ogg、WAV 等音频格式，删掉文件里附带的设备、软件、时间等标签。项目自己说得很清楚：它**只去元数据，不匿名化内容本身**。对留声来说正好：声音一点不动，只把文件外壳上可能指向某个人、某台手机的信息去掉。具体对每种音频格式清得多干净，搜索结果没说，现状未确认。[Debian 软件包](https://packages.debian.org/nl/buster/mat2)
- **浏览器里"关掉美化"并不可靠**：留声文档里写了要把 `echoCancellation`、`noiseSuppression`、`autoGainControl` 设为 false。WebKit 的 bug 记录显示，2017 年 Safari 曾直接无视这些设置（后来标记已修复）；2024 年又有一个仍未关闭的 bug：关掉回声消除后，iOS 和 macOS 的 Safari 会把单声道录成只有左声道有声音的立体声。Chrome 团队另写过一篇怎么关掉**硬件**降噪的文章，说明有些美化发生在浏览器之下。结论：网页版录不到真正的"原样"，要用 `track.getSettings()` 实测。[WebKit 281978](https://bugs.webkit.org/show_bug.cgi?id=281978) · [WebKit 179411](https://bugs.webkit.org/show_bug.cgi?id=179411) · [Chrome 博客](https://developer.chrome.com/blog/disabling-hardware-noise-suppression/)

### 今天的一个想法
昨天想的那面"存在过"的墙，可以直接用透明度日志搭，而且用不着信任留声自己。 每留下一段声音，就往一本只能追加的公开账本（Tessera）里写一行：这段录音的指纹。账本定期把自己的"总指纹"交给 OpenTimestamps 锚定到比特币，正好补上 Sigstore 承认的那个缺口：账本自己的时钟不可信，比特币的可信。账本是一块块静态文件，认同这件事的人可以整本镜像，像做种一样，留声哪天关了，墙还在，谁都能验证"某时某刻有一段声音写进来过，之后没人改过"。墙上没有名字、没有内容，进墙之前再用 mat2 这类工具把文件外壳上的设备信息去掉，声音本身一个字节都不动。Nonograph 说明"发出去就收不回"在开源世界里已经有人这样做，而且有人用。

### 可以继续挖
- Tessera 的 GA 版本和实际部署的例子（规模、成本），以及透明度日志和 OpenTimestamps 怎么组合，有没有现成做法
- 原生 App（iOS 的 AVAudioSession 的 measurement 模式、安卓的 UNPROCESSED 音源）能不能拿到真正未经处理的麦克风信号

## 2026-10-19 · 极客社区

### 发现
- **After the Beep：一个给全世界听的匿名语音信箱**：Hacker News 上有人分享的小项目（帖子标题"Anonymous public voicemail inbox"），2023 年春天上线，作者 Blaine Murphy。打一个美国号码留言，不问是谁，留言公开放在网站上。但每条都要作者**人工听过、审过**才上线，优先英文，有人留言几周后才出现。"公开可听"的代价是：总得有人先听一遍。HN 原帖和讨论没能打开，以下据报道。[Neoteo](https://www.neoteo.com/en/after-the-beep-lets-you-leave-anonymous-voicemail-for-the-world-to-hear) · [HN](https://news.ycombinator.com/item?id=39910119)
- **At The Beep：一条打算永远开着的匿名电话线**：任何人都能打进去说任何事，据播客目录介绍已攒下超过 17 万条语音，内容是爱、为人父母、死亡、成瘾、后悔。项目说要让这条线"无限期开着"，对外只放出随机挑选的一小部分做成播客。绝大多数声音其实没人听到，但它们在。数字来自目录页，现状未确认。[Podder](https://search.podderapp.com/podcast/at-the-beep)
- **Just2Voices：两个陌生人，一通电话，不留名字**：HN 上的开源项目，匿名语音通话，点对点直连，服务器只牵线，不录音、不留文字。它是留声的另一极：完全匿名，但什么都不留下。留声要的是匿名而且留下。HN 讨论页没能打开。[HN](https://news.ycombinator.com/item?id=48354414)
- **HN 上一句冷水：声音几乎不可能完全匿名**：在 HN 关于匿名语音的讨论里，有评论认为一段录音要彻底匿名"几乎不可能"。这和收窄后文档里写的"熟人一听就知道是谁"是同一件事。留声不处理声音，所以匿名只能做在"我们不知道是谁"这一层，没法做到"谁都听不出是谁"。原评论我没能打开核对。[HN](https://news.ycombinator.com/item?id=10422613)
- **V2EX 上的开源 24 小时录音工具 Eve**：作者主张先把原始声音留着，因为模型会进步，今天转得不好的音频以后可以用更好的模型重新处理。理由和留声"原样保存"一模一样，只不过 Eve 是给自己用的。据搜索摘要，原帖没能打开。[V2EX](https://v2ex.com/t/1193080)

### 今天的一个想法
"存在过"本身可以公开，而且不需要任何人先听。 After the Beep 说明，只要声音公开可听，就得有人先听一遍、审一遍，这和"录音加密、我们本来也听不到"正面冲突；At The Beep 说明，绝大多数声音其实没人听，它们的意义在于"在那条线上"。不管"世界能不能听到"最后怎么选，有一样东西三种选择都能用：一面公开的墙，每段声音在上面是一个点，只带它的指纹和 OpenTimestamps 的时间证明，不带名字、不带内容。任何人都能核对"某时某刻，这里有一段声音存在过"，却没人知道是谁、说了什么。原型页底部那一排红点，其实已经是这面墙的样子。这面墙要不要再往前一步、让点能被点开来听，留给你定。

### 可以继续挖
- After the Beep / At The Beep 这类匿名电话线怎么处理违法内容和下架请求，有没有人公开谈过运营成本
- 公开"指纹 + 时间"本身算不算个人信息、需不需要审核：指纹不可还原，理论上不含内容，值得找法规上的说法核实

## 2026-10-18 · 同类产品新闻

### 发现
- **Storyworth 推出 Story Calls：打电话就能讲故事**：老牌家族回忆录服务 Storyworth 加了电话功能，讲述人直接打电话回答，连座机都行，通话逐字转写。门槛降到了"会接电话就行"，是给不用智能手机的老人准备的。我没能打开原文，推出时间未确认。[The Next Web](https://thenextweb.com/news/storyworth-voice-tools-family-memory)
- **Heritage Whisper 上线：AI 采访员替你问奶奶**：2026 年 4 月在美国上线，创始人没能在祖母去世前听她讲完故事，于是做了一个叫 Pearl 的 AI 采访员，现场提问，录音加文字稿，最后攒成一本数字书。[Barchart](https://www.barchart.com/story/news/1185876/heritage-whisper-launches-platform-to-help-families-capture-stories-before-its-too-late)
- **语音回忆录 App 扎堆，方向几乎一致**：Sommos 用 AI 分析录音、把亲戚之间的回忆串起来；Heirloom4Life 让家人事后"向录过音的人提新问题"；ToldByMe 卖的是一次买断的"AI 润色"。整个市场在往"AI 提问、转文字、润色、成书、能对话"走，正好和留声的"不念稿、不处理、不生成"相反。[Technical.ly](https://technical.ly/entrepreneurship/sommos-ai-family-archive/)
- **《纽约客》：父亲还在世，女儿先做了他的"死亡机器人"**：2026 年 7 月的长篇报道，意大利一位艺术家在 77 岁父亲衰弱时，用回忆、照片等资料做了一个可对话的 AI 父亲，花费和订一个流媒体会员差不多。文章问的是：这样的复制品到底能给人什么。只读到转载的开头。[Bioethics.com 转载](https://bioethics.com/?p=103407)
- **又一个前车之鉴：Eternime 2018 年关闭**：早年的"数字永生"项目，因为找不到足够的用户而关闭。加上 HereAfter、StoryFile，这条赛道上倒下的名单又长了一截。[Ginger Liu](https://gingerliu.substack.com/p/technology-that-can-communicate-with)

### 今天的一个想法
**给不用智能手机的人一条"电话版"的留声：拿起电话就是按下按钮，挂断就是放手。** Storyworth 的电话功能说明，最需要留下声音的那群老人，往往卡在"装 App"这一步。留声的手势本来就和打电话同构：拿起听筒开始说，说完挂断，声音就留下了，没有时长，也没有"重来"。签署也可以在电话里完成，问一句"你为什么来这里"，回答就是签名和声纹样本。别人都在用 AI 采访员引导、润色、成书，留声反过来，只给一条安静的线路，接通之后不提示、不打断。这不改变任何已定的立场，只是多一个入口。

### 可以继续挖
- 电话入口的技术和成本：开源的电话交换软件（如 Asterisk、FreeSWITCH）能不能直接录下原始通话音质，国内运营电话号码需要什么资质
- Storyworth Story Calls 的具体推出时间和老人的实际使用反馈


## 2026-10-17 · 伦理法规

### 发现
- **《个人信息保护法》第四十九条：死者生前的安排优先**：近亲属为了自身合法、正当利益，可以对死者的个人信息行使查阅、复制、更正、删除等权利，但"死者生前另有安排的除外"。学者认为安排可以是遗嘱、授权协议或平台提供的机制；如果生前明确说死后谁都不许查阅，近亲属就无权查阅。这和留声"谁能听只选一次"正好对上：签署时的选择，有机会成为法律意义上的"生前安排"。近亲属的权利范围学界仍有分歧。[安全内参](https://www.secrss.com/articles/94168)
- **声纹是敏感个人信息，国标 GB/T 45574-2025 已生效**：《数据安全技术 敏感个人信息处理安全要求》2025 年 11 月 1 日起施行，是《个保法》在敏感信息上的细化。声纹属于生物识别信息，处理一般要取得**单独同意**。也就是说，签署流程里"我们会认得你的声音"那一句，需要单独一步明确同意，不能和其他规矩捆在一起。标准正文里针对声纹的具体条款我没能查到，现状未确认。[Morgan Lewis](https://www.morganlewis.com/pubs/2025/09/chinas-new-standard-on-sensitive-personal-information-goes-into-effect-november-1)
- **全国首例 AI 声音侵权案：声音是人格权益**：北京互联网法院 2024 年判决，配音师的声音被拿去做 AI 语音产品，判赔 25 万元。依据是《民法典》第 1023 条，声音参照肖像权保护；法院特别指出，**授权录音不等于授权对声音做 AI 化处理**。留声"原样保存，将来交给未来的人决定"，这里有一个现实约束：未来谁想拿这些声音做数字生命，需要有授权。只查到一审报道。[澎湃新闻](https://m.thepaper.cn/newsDetail_forward_27137070)
- **区块链信息服务要向网信办备案**：2019 年施行的《区块链信息服务管理规定》要求在境内提供区块链信息服务的主体在线备案，并在显著位置标明备案编号；技术支持方和链上节点也被纳入"提供者"范围。留声用 OpenTimestamps 锚定比特币，国内运营时是否需要备案、谁来备案，需要具体咨询。规定目前是否修订过，现状未确认。[君合](https://junhe.com/legal-updates/904)
- **《个人信息出境认证办法》2026 年 1 月 1 日施行**：向境外提供个人信息有安全评估、标准合同、认证几条路，敏感个人信息不满 1 万人可以走认证。录音和声纹放到 IPFS / Arweave，节点遍布全球，很可能构成"向境外提供"。去中心化存储具体怎么适用，官方没有说法，现状未确认。[国家网信办](https://www.cac.gov.cn/2025-10/17/c_1762449729500501.htm)

### 今天的一个想法
**把签署本身做成一份能被证明的"生前安排"。** 《个保法》第四十九条把死者生前的安排放在近亲属之前，而留声的签署恰好就是在定"解锁日期"和"谁能听"。如果签署的那段声音（签名 + 声纹）和所选的安排一起算出指纹，用 OpenTimestamps 锚定到链上，就有了一份"某年某月某日，本人亲口定下"的证据，不靠平台存证，也改不了。这和"只给一次机会"互相成全：正因为不能改，它才更像一份遗嘱。声纹那一句同意，按国标单独成一步，规矩里本来就写了，只是要单独确认。

### 可以继续挖
- 2026 年 7 月 15 日施行的《人工智能拟人化互动服务管理暂行办法》管的是"模拟人格的持续情感互动"，留声不做这个，但将来有人拿留声的声音做数字生命，就会落到它头上；办法里有没有关于逝者的条款，今天没能读到原文
- 北京石景山法院 2026 年认定游戏账号可以继承；留声的账户（和钥匙）在法律上算不算可继承的东西，值得找律师聊聊


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

