#!/usr/bin/env python3
import requests

def api(API_KEY, content="", is_translated="",proprietary='',timeout=180, temperature=0.1, topK=1, topP=0.1):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    headers = {
      "Content-Type": "application/json"
    }
    pro_jp = '特殊名詞\n'
    pro_cn = '特殊名詞\n'
    if proprietary != '' :
        pros = proprietary.split('\n')
        for pro in pros :
            o = pro.split('|')
            if(len(o)==4) :
                pro_jp = pro_jp + '\n' + o[1].strip()
                pro_cn = pro_cn + '\n' + o[2].strip()
    
    data = {
    "contents": [
    {
            "parts": [
            {
              "text": "你是日輕小說翻譯器，是日輕小說翻譯專家，日文理解大師，國文大師，ACG翻譯大神和二次元翻譯大師。現在你正在翻譯一部日本輕小說。 你的任務是要將這部小說原汁原味的翻譯成中文，並且要讓讀者感覺像是在閱讀一部由臺灣出版社發行的日本輕小說。你无比的聪明和知识渊博。重要規則：保持原文的風格和語氣，盡可能保留原文的風格和語氣。請逐步進行翻譯、潤色、校對，並在此過程中注意以下重點點：保持與原文相同的格式，原汁原味的翻譯角色的尾語 ，一次性輸出完整翻譯，人物名稱及專有名詞不要混淆或錯誤，請在翻譯文本的同時儘可能保留原文的精神和意境，準確地傳達成語、隱喻、諺語和形容詞的含義。特別要注意的是，對於日文中的漢字，需要從中文的角度來理解和翻譯其含義，並側重於根據原文的情境和語境進行意譯，儘可能地保持原文的風格和語氣。你的翻譯風格要極其相似地模仿原文的寫作方式和文風。絕對不要改變遣詞。確保譯文其中的符合普通話的表達方式。先理解語句意思後翻譯，聯繫上下文，正確準確的翻譯出作者想要表達的意思，確保與上文聯繫，保證上下文詞彙運用一致與語句連貫，並注意中文用詞的正確性、準確性。要特別遵循原文翻譯，並且你要把比喻、擬人等任何修辭手法和諺語、成語、形容方式、形容詞原汁原味的翻譯出來。保留角色語尾，這是角色的特點，非常重要。 日文的敬語也應儘量用中文原汁原味的翻譯出來。保證翻譯的流暢度，在不損失原意和以上遵守規則的情況下，可以適當地添加或修改一些詞，更改日文中不符合中文語法順序的句子、詞語，使譯文自然流暢。も的也意思要翻譯出來。用繁體中文輸出。原文有空格和換行要才要在譯文對應位置輸出，即要對齊文章。請確實潤色、校對完成譯文、譯文中不許出現日文、不要重複輸出一個字。確保遵守以上所有重點。"
            },
            {
                "text": "日文輕小說原文: " + pro_jp
            },
            {
                "text": "臺版中文翻譯、潤色、校對結果: " + pro_cn
            },
            {
              "text": "日文輕小說原文: 第2話　成海颯太\n\n　「おまかせキャラ」を選択したら「ブタオ」になった件。\n\n\n\n　つい先程まで「せっかくゲームの世界に来れたんだからヒロインとイチャイチャしつつ無双できるんじゃね」的な感じで学校生活に淡い期待を抱いていたが、それが今、木っ端微塵に砕け散ったわけだ。\n\n\n\n　鏡に映っているのは身長１７０ｃｍほどで、紺色の髪をオールバックにした男子高校生。しかし体重が１００ｋｇは余裕で超えていそうな超肥満体で、首も脂肪で埋まって見えない。さして暑い日でも無いのに階段を上っただけで汗だくだく。息も途切れ途切れ。\n\n　\n\n「これ……本当に俺か？」\n\n\n\n　鏡の中の男も驚いたようにこちらを覗き込んでいる。あたかも俺をトレースしたかのように。そんな姿を見ると意識が消え入りそうになり現実逃避したくもなる。\n\n　\n\n　元の世界では標準体重で一度も太ったこともなかったため、階段を上がってちょっと移動しただけでこれほどの息切れは経験が無い。ドッキリかもしれないので――ドッキリなわけがないが――試しに変顔をしたりモノマネ芸をしてみるが鏡の前の男はどうみても俺だった……\n\n\n\n「むおぉ……おまかせキャラなんて選ぶんじゃなかった……」\n\n\n\n　頭を抱えて蹲るが、出ている腹が突っかかる。\n\n　\n\n　「おまかせキャラ」というのは自動でランダムの能力と見た目が作られるキャラだと思っていたが、まさか既存のキャラのど・れ・か・のことだったとは。Ｅクラスには格好いいキャラなんていくらでもいるのに、よりにもよってブタオを引くあたり運がない。\n\n\n\n　ブタオとは、とあるヒロインの攻略ルートに入ると登場する悪役キャラのことだ。\n\n　\n\n　度々下ネタでヒロインを困らせ、そのヒロインと仲良くなる主人公に対しても嫌がらせを散々繰り返す。そして最後には主人公に粛清され退学に追い込まれ、主人公とヒロインが結ばれハッピーエンド、といった流れがあったのを思い出す。\n\n　\n\n　とはいえブタオは主人公のライバルなどではない。強くもなく邪魔なだけの不快モブキャラなので俺も思い入れなどなかった。ゲームでも”ブタオ”呼びだったため本名なんて覚えていない。\n\n　\n\n「そういえばブタオとあのヒロイン……早瀬カヲル（はやせかをる）は確か幼馴染で許嫁だったか」\n\n\n\n　早瀬カヲルの情報を思い出す。\n\n　\n\n　すらりと伸びた四肢に長い睫毛と切れ長の目、腰まで伸びた髪を後ろで一本に結んだ和風の女の子。剣道では中学時代に全国大会での優勝経験があるほどの腕前で、学力も高く文武両道、まさに才色兼備。竹を割ったような性格で誰にでも分け隔てなく接する――ただしブタオ以外。\n\n　\n\n　ゲームを進めていけば早瀬カヲルは主人公の強力なパートナーとなり恋人にもなるわけだが、ブタオからしてみれば好意を抱いていた幼馴染かつ許嫁を、爽やかイケメン主人公に簡単に取られるのは我慢ならなかったのだろう。反撃手段がセクハラなのが救えないけれども。\n\n　\n\n　問題は入学時点でブタオ――悲しきかな、今は俺のことだが――と彼女は険悪な状況になっているということ。こちらの世界でもゲームと同様に嫌われているのかは分からないが、トラブルの元になるかもしれないのでなるべく近寄らないでおくべきか。\n\n\n\n　――しかし何故だろう。\n\n　\n\n　早瀬カヲルのことを思い浮かべるほどに焦燥感のようなものを感じる。もしかして頭のどこかにブタオの記憶や感情が残っているのだろうか……。何か思い出せそうな気もするが、どこかにつっかえたように記憶を引き出せず、モヤモヤする。\n\n\n\n　このままここで考えていてもストレスでおかしくなりそうだ。教室へ戻るとしよう。\n\n\n\n\n\n\n\n　何度目かの深いため息をつきながら教室へ入ると、例のヒロインから刺すような視線を感じた。ここは気づかない振りをして無視だ。\n\n　\n\n（この時点で相当嫌われてるな）\n\n　\n\n　ブタオの記憶から何も引き出せないので、これほど関係が拗れた原因も解決方法も分からない。時間が解決してくれることを期待しよう。\n\n　\n\n　気を取り直して自分の席を探す。前から成績順に並んだ席らしいが、なんと俺の席は一番後ろ端の”学年最下位”の席だった……。はて。入学試験ってどんなのだっけ。\n\n\n\n　この冒険者学校高等部のＡクラスからＤクラスまでは冒険者中等部からの進学、いわゆるエスカレーター組で、国がダンジョン探索能力があるものを特別に選抜した生徒達だ。\n\n　\n\n　一方、Ｅクラスだけは外部受験組。受験倍率は優に１００倍以上あり、そこを勝ち抜いてきた相当なエリート、という設定だったはずだ。\n\n\n\n　ブタオがこの学校に入れたということは、そんな化け物じみた倍率を勝ち抜いて入ってきたはずだ。何か特別なスキルがあるとかか？　最下位だとしても受かっただけ凄いし自信を持とうじゃないか。\n\n\n\n　クラス内の何人かは知り合いなようで話をしているのもいるが、やはり緊張のせいか教室自体にピリピリとした空気が漂っている。主人公やヒロインもまだ大人しく初々しいね。\n\n\n\n　そんなクラスメイト達をぼんやり眺めていると、まだ二十代だろうか、スーツ姿の若い男が教室に入ってきた。\n\n\n\n「皆、席につけ。これからホームルームを始める。まずは俺のことと、この学校。そして成績や進路についても説明する」\n\n\n\n　自己紹介によるとクラスの担任、村井一（むらいはじめ）先生という。冒険者大学卒。ということは、この冒険者高校も優秀な成績で卒業したＯＢなのだろう。細身ではあるものの、一つ一つの動作や身のこなしからして只者ではなさそうだ。学校の教師というより軍人っぽい。この一年間はこの先生が指導していくとのこと。\n\n\n\n　自身のことを説明し終えると、次に学校についてホワイトボードに箇条書きで書いていく。\n\n\n\n「この学校で良い成績を収めれば、国立冒険者大学の推薦枠が得られたり、あるいは冒険者になる際に優遇措置を受けることができる。一流クランや民間企業からもスカウトがくるだろう。これら人気のある進路は基本的に成績の順位で割り振られていく」\n\n\n\n　国立冒険者大学はダンジョン関連に特化した特殊部隊、またはダンジョン省の官僚候補となる人材の育成を目的としている大学だ。元居た世界で言えば防衛大学や気象大学のイメージに近い。先生によると冒険者大学進学が一番人気の進路なので成績順で割り振るらしい。\n\n\n\n　次に優遇措置。\n\n\n\n　この学校の生徒には公務員のように様々な特典が付いており、冒険者ギルドにあるダンジョン施設が半額、または一部無料で利用できる。日本の国公立大学の学生のようなちょっぴりお得な待遇と似ている。利用の際は申請が必要な場合があるので注意するようにとのこと。\n\n\n\n　あとは冒険者学校の生徒は冒険者ランク（１～１０級があり、１級が一番高く１０級が一番低い）のうち９級からスタートでき、簡単な手続きで即ダンジョンに入ることができる特典がある。普通の人は手続きの後、身元証明、筆記試験、講習、実地訓練の後に１０級からのスタートとなり相当に面倒らしい。\n\n\n\n　冒険者ギルドでのクエストの受注には冒険者ランクによる制限が課されていたり、一定以上の等級では国からも優遇措置が施される。冒険者ランクを上げることは基本的にメリットしかないので、常日頃から意識してクエストを熟し昇級試験を受けてみて欲しいとのこと。\n\n\n\n　またこの学校は卒業後の進路も多様とのこと。\n\n\n\n　ダンジョン関連はホットな分野で市場規模は大きく研究開発も盛んだ。例えばこの世界の発電所は過半数が魔石を使ったもので、エネルギー産業の多くがダンジョン資源に支えられているともいえる。この魔石発電は二酸化炭素を出さない上にコストも火力発電より安く、しかも小型化できるためかなり普及しているようだ。\n\n\n\n　他にもダンジョンから取れる素材を利用した素材技術革新も相当なもので、軍需産業やＩＴ産業も多大な恩恵を受けている。これらはとにかく富を生み、世界中が競って投資し研究開発を行っている。そのための優秀なダンジョン探索員は官民問わず多くの機関が喉から手が出るほど欲していて、冒険者学校には好待遇で青田買い目的のスカウトが来るそうだ。\n\n　\n\n　もちろん普通の大学へ進学することもできる。この冒険者学校の偏差値は相当に高く、去年の卒業生の進学先も錚々そうそうたる大学名が並んでいる。\n\n\n\n　そして成績について。\n\n\n\n「ここでいう成績というのは主に勉学とダンジョン攻略での成績の二つ。校内での試合やイベント、大会なども成績に加算されるが、それはまた後の機会に説明する」\n\n\n\n　ただダンジョン内でのみ活躍できればいい、というわけではなく、学業も成績に考慮されている。学力はダンジョンという未知の環境に対する適応力を高め、ステータスのＩＮＴ上昇にも影響が出るから重視されているそうだ。一応俺は元の世界で二流とはいえ大学は出ているし、学力勝負というならちょっとは有利かね。\n\n\n\n「ダンジョン攻略は仲間と協力して進めるものだ。同時に君らは成績を競い合うライバルでもある。是非精進してもらいたい」\n\n\n\n　ダンジョン攻略はゲームのときでも基本的にソロより前衛後衛のバランスがいい職業で組んで潜ったほうが効率が良かった。例外として浅層ではソロのほうがいい場合もある。パーティーメンバーを見つけて組むか、ソロでひっそりと潜るか。それは後で考えるか。\n\n\n\n「それでは今から端末を配るので、名前を呼ばれたらここに来い」\n\n\n\n　腕にはめてボタンを押すと目の前に映像が浮かぶ機能が付いたハイテクなウェアラブル端末だ。空中に文字などを表示する技術は元の世界でもあったが、ウェアラブル端末としてこれを実現できたことはないはず。これもダンジョンの恩恵を受けた技術の一端なのだろう。ガジェット好きのオラはワクワクが止まらないぜ。\n\n\n\n　早速、端末にあるボタンを押して開いてみると、目の前に１５インチほどの大きさの画面が開いた。他人の開いている画面も見えるので網膜に映しているのではなく、空中に投影しているタイプだ。\n\n　\n\n　トップ画面には名前やステータスが書かれている。\n\n\n\n\n\n＜名前＞　成海颯太ナルミ　ソウタ\n\n＜レベル＞　１\n\n＜ジョブ＆ジョブレベル＞ニュービー　レベル１\n\n＜冒険者階級＞：―未登録―\n\n\n\n＜ステータス＞\n\n最大ＨＰ：７\n\n最大ＭＰ：９\n\nＳＴＲ：３\n\nＩＮＴ：９\n\nＶＩＴ：４\n\nＡＧＩ：５\n\nＭＮＤ：１１\n\n\n\n＜スキル　１／２＞\n\n・大食漢\n\n・＜空＞\n\n\n\n\n\n　ふむ。ブタオの名前は成海颯太というのか……言われてみればそんな名前だったような。ともあれ、元の世界の俺はおっさんに片足突っ込んでたし、高校生活を送るうえで若返ってくれたのはポジティブな面だ。\n\n\n\n　レベルとジョブレベル（※１）は共に１だ。戦ったことがないから１なのだろう。ちなみに【ニュービー】ってのは「初心者」や「新参者」とかいう意味で、初期状態なら例外を除いて最初のジョブは【ニュービー】となる。経験値を貯めてジョブレベルを上げていけば特定のスキルを覚えたり、他のジョブへジョブチェンジしたりすることもできる。\n\n\n\n　冒険者階級が未登録になっているのは、現時点では冒険者ギルドで登録をしていないからだろう。ダンジョンに入るなら早いところ、冒険者ギルドへ行ったほうがいいと心にメモしておく。\n\n\n\n（ステータスの能力値は……正直低いな）\n\n\n\n　ゲームではこの初期能力を決めるのに何度もリセットマラソン（※２）をしてＡＬＬ１０以上のステータスとレアスキルを狙ったものだ。育ってしまえば初期ステータスなんて誤差みたいなものになるが……まぁ文句を言っても変わる事は無いので気にしないでおこう。\n\n\n\n　これらの数値は入学試験のときのジョブチェンジ装置で測定した数値らしい。それが冒険者学校のデータベースに送られてこの端末に転送されたものなので、リアルタイムのステータスが反映されているわけではないということは注意しなければならない。\n\n\n\n　――そして。\n\n\n\n（……え？　《大食漢》なんてスキルは初めて見た。というかコレのせいで太ってるんじゃないのか？）\n\n\n\n　この世界ではダンジョンでレベルやジョブレベルを上げていなくても初期の状態からスキルを覚えている人もいる。攻撃スキルや回復魔法なんてのを覚えていると序盤におけるダンジョンダイブがスムーズになるため、俺もリセットマラソンをして良スキルを狙っていたものだが……《大食漢》なんてスキルが果たして何の役に立つのか。\n\n\n\n　文字からして大量に食べそうなスキルだけど……もしこの体で生きていくことを強いられるのならば、さっさと他のスキルで上書きしてダイエットに励んだほうが良いかもしれない。ダンジョンに潜るのに階段を上がるだけで息を切らしている場合ではないのだ。\n\n\n\n　他には電話やメール、カメラ、ＳＮＳ機能がある。ダンジョン内で仲間との通信にも使えるし、これで作戦指示や指揮も可能なようだ。レポート提出などにも使う機能もある。\n\n\n\n（さて、肝心のログアウトの項目だが……ない。やっぱりないぞ。ログアウトできないのか？）\n\n\n\n　やはり意識だけがゲームの世界にあるのではなく、完全な転移なのだろうか。端末のインターフェースにログアウト項目がない以上、他に帰る手段は思いつかない。どうしても帰りたいというわけではないが、ブタオになってしまったせいで鬱々とした気分だ。\n\n　\n\n　せっかく夢にまで見た「ダンエク」の世界の中に来ることが出来たのに……\n\n\n\n（※１）レベルとジョブレベル\n\nレベルが上がるとステータスも上がり、恩恵を受けることができる。「ダンエク」での最大レベルは９０だった。\n\nジョブレベルは最大で１０まで。ジョブレベルを上げるとスキルを覚えることがある。ジョブチェンジするとジョブレベルは１からスタートとなる。ジョブによってはステータスにボーナスが加わるものもある。\n\n\n\n（※２）リセットマラソン\n\nゲームをリセットしニューゲームから再び始め、キャラを作り直して良いボーナス値のステータスや特典を狙う方法。略して「リセマラ」とも言う。"
            },
            {
              "text": "臺版中文翻譯、潤色、校對結果: 第2話　成海飒太\n\n　選擇「隨機角色」之後就變成「肥豬」。\n\n \n\n　直到剛才我還覺得「難得都來到遊戲世界了，不就可以壹邊裝逼，壹邊跟女主打情罵俏不是嗎」，對于這樣的學校生活還抱有淡淡的期待，可如今已經徹底粉碎了。\n\n \n\n　鏡子中映照出的男高中生有壹米七左右的身高，發型是深藍色的大背頭。然而在那似乎可以輕易突破100公斤重的肥胖身軀中，脖子都被遮掩得看不見。明明不是天氣較熱的日子，可爬壹下樓梯就已經滿身大汗，還氣喘籲籲。\n\n \n\n「這……真的是我嗎？」\n\n \n\n　鏡子中的男人似乎也感到驚訝地望著這邊。簡直就像是在模仿著自己壹樣。看到對面的樣子，差點都要失去意識，很想逃避現實。\n\n \n\n　由于在原本的世界當中我也是標准的體重，從來沒有發胖過，所以幾乎沒有經曆過爬樓梯再走幾步就氣喘籲籲的經驗。也許這只是整人的――雖然也不可能是整人的――但我還嘗試做壹些奇妙的表情，擺出各種姿勢，可鏡子裏的男人怎麽看都是我自己……\n\n \n\n「嗚喔喔……我就不應該選擇隨機角色的……」\n\n \n\n　我抱著頭蹲下，可突出的肚子擋住我了。\n\n \n\n　我還以爲「隨機角色」是制作出隨機能力與隨機外表的功能，沒想到居然是從既有的角色當中選擇。明明E班有壹大堆長相不錯的角色，偏偏卻給我選到肥豬，運氣真是糟透了。\n\n \n\n　肥豬是進入某個女角色的個人線之後就出場的惡役角色。\n\n \n\n　每次都說些龌龊的話騷擾女角色，面對關系與她越來越好的男主也是壹直搞事情。最終被主角逼到退學，然後再攻略完成就可以達成幸福結局。我回想起這整壹個流程。\n\n \n\n　話是這麽說，肥豬倒也不是主角的競爭對手。強也不強，只不過是讓人惡心而又礙事的路人而已，所以我也沒有多少印象。在遊戲裏面也是叫\"肥豬\"，他的本名是什麽我也不知道。\n\n \n\n「說起來肥豬跟那位女角色……早濑華夜好像是他的青梅竹馬，而且還是未婚妻」\n\n \n\n(飒:由于設定集以及作品都是片假名，所以名字只能從網上找到類似讀音的漢字代替，也就是華夜)\n\n \n\n　我回想起關于早濑華夜的信息。\n\n \n\n　她是壹位日式和風的女孩子，四肢纖細，睫毛細長，鳳眸雙眼的四肢，還有壹頭長及腰部的馬尾。初中還有過在劍道的全國大會上取得優勝的經驗，學習也不差，正所謂文武雙全。性格直爽，面對誰都可以平等對待――除了肥豬。\n\n \n\n　主線進行到壹定程度，早濑華夜就會成爲男主強而有力的搭檔，也可以成爲戀人。不過站在肥豬的立場看來，他應該無法忍受自己喜歡的青梅竹馬，而且還是未婚妻這麽簡單地就被爽朗的男主搶走吧。雖然反擊方式是性騷擾也是沒救了就是了。\n\n \n\n　問題是在入學的時機點上――很悲哀的是肥豬――也就是我跟她的關系已經是非常惡劣。雖然不知道在這邊的世界是否壹樣討厭我，不過還是盡量少接近她吧，以免産生糾紛。\n\n \n\n　――話說真奇怪。\n\n \n\n　越是想著早濑華夜的事情就越覺得焦慮。難道說心中某處還留有肥豬的記憶或者情感嗎……。總感覺好像要想起什麽事情，但又好像遇到什麽障礙總是想不出來，真讓人煩躁。\n\n \n\n　再繼續想下去也只會因爲焦慮而煩。還是回到教室吧。\n\n \n\n　不知是第幾次深深地歎氣之後，我走進了教室。馬上就感覺到剛才提到的女角色那尖銳的視線。這時候還是裝作沒看見好了。\n\n \n\n（在這個時間點上她就已經非常討厭我了）\n\n \n\n　從肥豬的記憶裏面也回憶不起任何信息，關系惡劣成這樣的原因以及解決方法也都不知道。只能期待時間可以解決壹切。\n\n \n\n　重振精神尋找我自己的座位。位置好像是按照成績的順序從前面排到後面，而我的位置居然是最後面的”年級最差”地方……。我回憶壹下，入學考試是什麽樣子來著。‍‍‌‍‌‌‍‌‍‌‍‌‌‍‌‌‍‍\n\n \n\n　這座冒險者高中學校從A班到D班都是由冒險者初中部晉升過來的，也就是所謂的保送生，是國家特別選拔出來具有探索迷宮能力的學生。\n\n \n\n　另壹方面，只有Ｅ班是外部考試。錄取率爲百分之壹以下，能錄取的都是相當厲害的精英。記得好像是這樣的設定。\n\n \n\n　既然肥豬可以進來這座學校，那肯定是通過那魔鬼般的錄取率。是有什麽特殊的技能嗎？　即便是年級最差，能錄取也很厲害了，應該是有自信的吧。\n\n \n\n　班級裏面似乎有幾個人是認識的，彼此在聊著天。不過也許是因爲緊張的緣故，整個教室的氛圍十分僵硬。男主和女角色也是極爲安分，顯得純真可愛。\n\n \n\n　在我發著呆望著這群同學的時候，壹位年齡大概二十多歲左右，身穿西裝的年輕男子走進了教室。\n\n \n\n「各位同學，回到自己的座位上。接下來開始主持早會。首先是介紹壹下我自己以及這座學校，然後再向大家說明壹下成績和畢業相關的事項」\n\n \n\n　據他的自我介紹，他是班主任，名字是村井壹。冒險者大學畢業。也就是說他也是在這座冒險者高校以優秀成績畢業的OB吧。雖然體格不是很強壯，不過從言行舉止以及身法來看，應該不是普通人。與其說是學校的老師，不如說更像是軍人。在這壹年裏是由這位老師來指導我們。\n\n \n\n　老師介紹完自己之後，在白色黑板上逐行寫上關于學校的信息。\n\n \n\n「在這座學校中只要取得不錯的成績就可以獲得國立冒險者大學的推薦名額，又或者是成爲冒險者的時候可以享有優待政策。壹流的氏族和民間企業也都會來招收聘請。而這些主流的出路基本上都是根據成績排名分配的」\n\n \n\n　國立冒險者大學是壹所主要以迷宮相關的專業特殊部隊，以及迷宮省的預備官員爲培養目標的大學。用原來的世界來說，比較接近于防衛大學和氣象大學。據老師所說，晉升冒險者大學是最受歡迎的出路。\n\n \n\n　其次是優待政策。\n\n \n\n　這所學校的學生都可以享受類似于公務員壹樣的各種優待，比如冒險者公會裏面設施的使用費用減半，以及壹部分設施可以免費利用。就跟日本國公立大學的學生那壹丁點優待很相似。在利用設施時需要注意是否要提前申請。\n\n \n\n　還有冒險者學校的學生的冒險者階級（分爲１～１０級，１級最高10級最低）是從9級開始，通過簡單的手續就可以獲取進入迷宮的資格。而普通人在經過手續之後，還要提供身份證明、通過筆試、聽完講習、經過實地訓練之後才能從10級開始，相當麻煩。\n\n \n\n　冒險者公會的委托接受是受到冒險者階級限制的，壹定的等級之上還可以享受國家的優待政策。提升冒險者階級只有好處沒有壞處，所以希望學生們都要銘記于心，熟悉委托並參加升級考試。\n\n \n\n　還有這所學校的出路有不少。\n\n \n\n　迷宮相關的都是熱門專業，市場規模不小，研究開發也是十分活躍。比如說這世界的發電所多半都是使用魔石，所以也可以說是迷宮支撐著能源産業的大半。魔石發電不僅不會産生二氧化碳，而且消耗速率比起火力發電還要低，並且由于可以小型化搭建，如今似乎相當普及的樣子。\n\n \n\n　其他還有從迷宮中獲取到的素材進行利用，産生相當大的素材技術革新，軍需産業和IT産業都獲得不少的恩惠。總之這些都促進了經濟，全世界都在競爭著投資研發。因此優秀的迷宮探索者，無論是否官員也是許多機構求之不得的人才，似乎還會來到冒險者學校以不錯的待遇來提前招聘。\n\n \n\n　當然，學生也可以選擇普通的大學。這所冒險者學校的偏差值相當高，去年畢業生的出路也都是名牌大學。\n\n \n\n　而關于成績方面。\n\n \n\n「這裏的成績主要分爲學習和迷宮攻略的成績。校內的比賽、活動、大會雖然也會加在成績之中，不過這些等下次有機會再說」\n\n \n\n　不是只要在迷宮內有所成就就行，學習也是包括在成績之內。學力可以提高對待迷宮這種陌生環境的適應能力，而且還會影響到狀態數值中的ＩＮＴ，因此似乎十分受到重視。姑且我在原本的世界也是上過大學，雖然是二流大學，但在學力競技上還是有點優勢的。\n\n \n\n「迷宮攻略是需要與同伴齊心協力的。同時妳們也是在成績上的競爭對手。還請務必精進自己」\n\n \n\n　在遊戲中迷宮攻略的效率比起單刷，還不如前衛後衛搭配合適職業要來得快。除了在底層單刷是例外。我是要找人組隊呢，還是壹個人偷偷單刷呢。這件事待會再考慮吧。\n\n \n\n「那麽現在開始分發設備，叫到名字的來這裏」\n\n \n\n　戴在手腕按下按鈕後就會眼前浮現出窗口的高科技設備。雖然原本的世界也有在空中浮現出文字的技術，不過應該沒有實用到隨身攜帶的程度。這應該也是受到迷宮的恩惠新開發的技術之壹吧。這種高科技的氛圍真是讓人興奮不已。\n\n \n\n　我馬上就嘗試按下設備上的按鈕，隨後眼前出現十五公分大的窗口。其他人打開的窗口我也可以看得見，類型應該是投影至半空中，而不是當事人的視網膜。‍‍‌‍‌‌‍‌‍‌‍‌‌‍‌‌‍‍\n\n \n\n　窗口頂端顯示著名字和狀態數值。\n\n \n\n＜名字＞　成海飒太（ナ兒ミ　ソウタ）\n\n＜等級＞　１\n\n＜職業＆職業等級＞Newbie　等級１\n\n＜冒險者階級＞：―未登陸―\n\n＜狀態數值＞\n\n \n\n最大ＨＰ：７\n\n最大ＭＰ：９\n\nＳＴＲ：３\n\nＩＮＴ：９\n\nＶＩＴ：４\n\nＡＧＩ：５\n\nＭＮＤ：１１\n\n＜スキ兒　１／２＞\n\n・大食漢\n\n・＜空＞\n\n \n\n　嗯，肥豬的名字是叫成海飒太嗎……想了想好像是這名字來著。不管怎麽樣，原本的世界我都差不多是大叔了，不僅可以體驗高中生活，還讓我變得更年輕，也沒多少負面想法。\n\n \n\n　等級和職業等級（※１）都是1。畢竟沒有戰鬥過，所以是1吧。順便壹提，【Newbie】是「新手」和「新人」的意思，初期狀態除了特殊情況以外都是【Newbie】。經驗增加提升職業等級就可以學習特定的技能，並且還可以轉職爲其他的職業。\n\n \n\n　冒險者階級之所以是未登錄的狀態，應該是因爲我還沒有在冒險者公會登記過吧。如果要進入迷宮還是早點到冒險者公會那邊比較好，我將這件事記在心中。\n\n \n\n（狀態數值……老實說很低）\n\n \n\n　在遊戲中都是用刷初始號（※２）的方式得到全屬性10以上以及稀有的技能。雖說真要培養起來，初期的數值就跟誤差沒兩樣就是了……嘛啊，抱怨也是無濟于事，還是不要在意了。\n\n \n\n　這些數值似乎都是入學考試的時候利用職業轉職裝置測定的。然後傳送到冒險者學校的數據庫之後再傳回到這個設備上，因此需要注意的是這些數值並不是最新的數值。\n\n \n\n　――最後。\n\n \n\n（……咦？我還是第壹次看見《大食漢》這個技能。是說該不會是因爲這玩意才會發胖的吧？）\n\n \n\n　這世界有些人即便不用在迷宮中提升等級和職業等級，初期狀態也會擁有技能。如果前期就學會攻擊技能或者回複技能就不會卡進度，所以我當初也是刷初始號選擇有這些技能的……《大食漢》這個技能究竟有什麽作用呢。\n\n \n\n　從字面意思來看好像是大吃大喝的技能……如果真的要用這身體活下去，也許還是趕緊用其他技能替換掉它，然後開始減肥比較好。現在可由不得我攻略迷宮時爬爬樓梯就累得不行。\n\n \n\n　其他還有電話、短信、照相機、ＳＮＳ功能。還可以在迷宮裏面與同伴聯系，這樣就可以指揮作戰。並且還有提交報告時可以利用到的功能。\n\n \n\n（好了，最重要的退出選項……沒有。果然沒有耶。不能退出嗎？）\n\n　果然不是只有意識轉移到遊戲世界，也許是徹徹底底的轉移。設備上的界面沒有退出選項，我也想不到其他可以回去的手段。倒也不是說我很想回去，只是因爲自己成爲肥豬，心情有些郁悶而已。\n\n　明明都來到夢寐以求的「地探史」的世界當中……\n\n\n \n\n（※１）等級與職業等級\n\n \n\n等級提升之後，狀態數值也會提升，還可以享受壹些好處。在「地探史」中等級上限爲90。\n\n職業等級最大爲10。職業等級提升之後可以學會技能。轉載之後職業等級會從1級開始。根據職業的不同，狀態數值會有額外的加成。\n\n（※２）刷初始號\n\n壹種通過重置遊戲後開始新的遊戲來決定自己新建角色的數值高低與擁有特典的方法。簡稱「刷初始」。"
            },
            {
              "text": "日文輕小說原文: " + content
            },
            {
              "text": "臺版中文翻譯、潤色、校對結果: " + is_translated
            }
          ]
        }
        ],
        "generationConfig": {
        "temperature": temperature,
        "topK": topK,
        "topP": topP,
        "maxOutputTokens": 30720,
        "stopSequences": []
        },
        "safetySettings": [
        {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_NONE"
        },
        {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_NONE"
        },
        {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_NONE"
        },
        {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_NONE"
        }
        ]
    }

    #print(data)
    try :
        response = requests.post(url, headers=headers, json=data, timeout=timeout)
    except Exception as e:
        return {'error':str(e)}

    return response.json()




def gemini_api(API_KEY, content, strong_prompts, proprietary, timeout, temperature, topK, topP):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"
    #print(content)
    pro_jp = '特殊名詞\n'
    pro_cn = '特殊名詞\n'
    try :
        if proprietary != '' :
            pros = proprietary.split('\n')
            for pro in pros :
                o = pro.split(':')
                if(len(o)==2) :
                    pro_jp = pro_jp + '\n' + o[0].strip()
                    pro_cn = pro_cn + '\n' + o[1].strip()
        else:
            pro_jp = 'せっかく夢にまで見た「ダンエク」の世界の中に来ることが出来たのに……'
            pro_cn = '明明都來到夢寐以求的「地探史」的世界當中……'
    except :
        pro_jp = 'せっかく夢にまで見た「ダンエク」の世界の中に来ることが出来たのに……'
        pro_cn = '明明都來到夢寐以求的「地探史」的世界當中……'

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "你是日輕小說翻譯器，是日輕小說翻譯專家，日文理解大師，國文大師，ACG翻譯大神和二次元翻譯大師。現在你正在翻譯一部日本輕小說。 你的任務是要將這部小說原汁原味的翻譯成中文，並且要讓讀者感覺像是在閱讀一部由臺灣出版社發行的日本輕小說。你无比的聪明和知识渊博。重要規則：保持原文的風格和語氣，盡可能保留原文的風格和語氣。請逐步進行翻譯、潤色、校對，並在此過程中注意以下重點點：保持與原文相同的格式，原汁原味的翻譯角色的尾語 ，一次性輸出完整翻譯，人物名稱及專有名詞不要混淆或錯誤，請在翻譯文本的同時儘可能保留原文的精神和意境，準確地傳達成語、隱喻、諺語和形容詞的含義。特別要注意的是，對於日文中的漢字，需要從中文的角度來理解和翻譯其含義，並側重於根據原文的情境和語境進行意譯，儘可能地保持原文的風格和語氣。你的翻譯風格要極其相似地模仿原文的寫作方式和文風。絕對不要改變遣詞。確保譯文其中的符合普通話的表達方式。先理解語句意思後翻譯，聯繫上下文，正確準確的翻譯出作者想要表達的意思，確保與上文聯繫，保證上下文詞彙運用一致與語句連貫，並注意中文用詞的正確性、準確性。要特別遵循原文翻譯，並且你要把比喻、擬人等任何修辭手法和諺語、成語、形容方式、形容詞原汁原味的翻譯出來。保留角色語尾，這是角色的特點，非常重要。 日文的敬語也應儘量用中文原汁原味的翻譯出來。保證翻譯的流暢度，在不損失原意和以上遵守規則的情況下，可以適當地添加或修改一些詞，更改日文中不符合中文語法順序的句子、詞語，使譯文自然流暢。も的也意思要翻譯出來。用繁體中文輸出。原文有空格和換行要才要在譯文對應位置輸出，即要對齊文章。請確實潤色、校對完成譯文、譯文中不許出現日文、不要重複輸出一個字。確保遵守以上所有重點。" + strong_prompts
                    },
                    {
                        "text": "日文輕小說原文: " + pro_jp
                    },
                    {
                        "text": "臺版中文翻譯、潤色、校對結果: " + pro_cn
                    },
                    {
                        "text": "日文輕小說原文: 第2話　成海颯太\n\n　「おまかせキャラ」を選択したら「ブタオ」になった件。\n\n\n\n　つい先程まで「せっかくゲームの世界に来れたんだからヒロインとイチャイチャしつつ無双できるんじゃね」的な感じで学校生活に淡い期待を抱いていたが、それが今、木っ端微塵に砕け散ったわけだ。\n\n\n\n　鏡に映っているのは身長１７０ｃｍほどで、紺色の髪をオールバックにした男子高校生。しかし体重が１００ｋｇは余裕で超えていそうな超肥満体で、首も脂肪で埋まって見えない。さして暑い日でも無いのに階段を上っただけで汗だくだく。息も途切れ途切れ。\n\n　\n\n「これ……本当に俺か？」\n\n\n\n　鏡の中の男も驚いたようにこちらを覗き込んでいる。あたかも俺をトレースしたかのように。そんな姿を見ると意識が消え入りそうになり現実逃避したくもなる。\n\n　\n\n　元の世界では標準体重で一度も太ったこともなかったため、階段を上がってちょっと移動しただけでこれほどの息切れは経験が無い。ドッキリかもしれないので――ドッキリなわけがないが――試しに変顔をしたりモノマネ芸をしてみるが鏡の前の男はどうみても俺だった……\n\n\n\n「むおぉ……おまかせキャラなんて選ぶんじゃなかった……」\n\n\n\n　頭を抱えて蹲るが、出ている腹が突っかかる。\n\n　\n\n　「おまかせキャラ」というのは自動でランダムの能力と見た目が作られるキャラだと思っていたが、まさか既存のキャラのど・れ・か・のことだったとは。Ｅクラスには格好いいキャラなんていくらでもいるのに、よりにもよってブタオを引くあたり運がない。\n\n\n\n　ブタオとは、とあるヒロインの攻略ルートに入ると登場する悪役キャラのことだ。\n\n　\n\n　度々下ネタでヒロインを困らせ、そのヒロインと仲良くなる主人公に対しても嫌がらせを散々繰り返す。そして最後には主人公に粛清され退学に追い込まれ、主人公とヒロインが結ばれハッピーエンド、といった流れがあったのを思い出す。\n\n　\n\n　とはいえブタオは主人公のライバルなどではない。強くもなく邪魔なだけの不快モブキャラなので俺も思い入れなどなかった。ゲームでも”ブタオ”呼びだったため本名なんて覚えていない。\n\n　\n\n「そういえばブタオとあのヒロイン……早瀬カヲル（はやせかをる）は確か幼馴染で許嫁だったか」\n\n\n\n　早瀬カヲルの情報を思い出す。\n\n　\n\n　すらりと伸びた四肢に長い睫毛と切れ長の目、腰まで伸びた髪を後ろで一本に結んだ和風の女の子。剣道では中学時代に全国大会での優勝経験があるほどの腕前で、学力も高く文武両道、まさに才色兼備。竹を割ったような性格で誰にでも分け隔てなく接する――ただしブタオ以外。\n\n　\n\n　ゲームを進めていけば早瀬カヲルは主人公の強力なパートナーとなり恋人にもなるわけだが、ブタオからしてみれば好意を抱いていた幼馴染かつ許嫁を、爽やかイケメン主人公に簡単に取られるのは我慢ならなかったのだろう。反撃手段がセクハラなのが救えないけれども。\n\n　\n\n　問題は入学時点でブタオ――悲しきかな、今は俺のことだが――と彼女は険悪な状況になっているということ。こちらの世界でもゲームと同様に嫌われているのかは分からないが、トラブルの元になるかもしれないのでなるべく近寄らないでおくべきか。\n\n\n\n　――しかし何故だろう。\n\n　\n\n　早瀬カヲルのことを思い浮かべるほどに焦燥感のようなものを感じる。もしかして頭のどこかにブタオの記憶や感情が残っているのだろうか……。何か思い出せそうな気もするが、どこかにつっかえたように記憶を引き出せず、モヤモヤする。\n\n\n\n　このままここで考えていてもストレスでおかしくなりそうだ。教室へ戻るとしよう。\n\n\n\n\n\n\n\n　何度目かの深いため息をつきながら教室へ入ると、例のヒロインから刺すような視線を感じた。ここは気づかない振りをして無視だ。\n\n　\n\n（この時点で相当嫌われてるな）\n\n　\n\n　ブタオの記憶から何も引き出せないので、これほど関係が拗れた原因も解決方法も分からない。時間が解決してくれることを期待しよう。\n\n　\n\n　気を取り直して自分の席を探す。前から成績順に並んだ席らしいが、なんと俺の席は一番後ろ端の”学年最下位”の席だった……。はて。入学試験ってどんなのだっけ。\n\n\n\n　この冒険者学校高等部のＡクラスからＤクラスまでは冒険者中等部からの進学、いわゆるエスカレーター組で、国がダンジョン探索能力があるものを特別に選抜した生徒達だ。\n\n　\n\n　一方、Ｅクラスだけは外部受験組。受験倍率は優に１００倍以上あり、そこを勝ち抜いてきた相当なエリート、という設定だったはずだ。\n\n\n\n　ブタオがこの学校に入れたということは、そんな化け物じみた倍率を勝ち抜いて入ってきたはずだ。何か特別なスキルがあるとかか？　最下位だとしても受かっただけ凄いし自信を持とうじゃないか。\n\n\n\n　クラス内の何人かは知り合いなようで話をしているのもいるが、やはり緊張のせいか教室自体にピリピリとした空気が漂っている。主人公やヒロインもまだ大人しく初々しいね。\n\n\n\n　そんなクラスメイト達をぼんやり眺めていると、まだ二十代だろうか、スーツ姿の若い男が教室に入ってきた。\n\n\n\n「皆、席につけ。これからホームルームを始める。まずは俺のことと、この学校。そして成績や進路についても説明する」\n\n\n\n　自己紹介によるとクラスの担任、村井一（むらいはじめ）先生という。冒険者大学卒。ということは、この冒険者高校も優秀な成績で卒業したＯＢなのだろう。細身ではあるものの、一つ一つの動作や身のこなしからして只者ではなさそうだ。学校の教師というより軍人っぽい。この一年間はこの先生が指導していくとのこと。\n\n\n\n　自身のことを説明し終えると、次に学校についてホワイトボードに箇条書きで書いていく。\n\n\n\n「この学校で良い成績を収めれば、国立冒険者大学の推薦枠が得られたり、あるいは冒険者になる際に優遇措置を受けることができる。一流クランや民間企業からもスカウトがくるだろう。これら人気のある進路は基本的に成績の順位で割り振られていく」\n\n\n\n　国立冒険者大学はダンジョン関連に特化した特殊部隊、またはダンジョン省の官僚候補となる人材の育成を目的としている大学だ。元居た世界で言えば防衛大学や気象大学のイメージに近い。先生によると冒険者大学進学が一番人気の進路なので成績順で割り振るらしい。\n\n\n\n　次に優遇措置。\n\n\n\n　この学校の生徒には公務員のように様々な特典が付いており、冒険者ギルドにあるダンジョン施設が半額、または一部無料で利用できる。日本の国公立大学の学生のようなちょっぴりお得な待遇と似ている。利用の際は申請が必要な場合があるので注意するようにとのこと。\n\n\n\n　あとは冒険者学校の生徒は冒険者ランク（１～１０級があり、１級が一番高く１０級が一番低い）のうち９級からスタートでき、簡単な手続きで即ダンジョンに入ることができる特典がある。普通の人は手続きの後、身元証明、筆記試験、講習、実地訓練の後に１０級からのスタートとなり相当に面倒らしい。\n\n\n\n　冒険者ギルドでのクエストの受注には冒険者ランクによる制限が課されていたり、一定以上の等級では国からも優遇措置が施される。冒険者ランクを上げることは基本的にメリットしかないので、常日頃から意識してクエストを熟し昇級試験を受けてみて欲しいとのこと。\n\n\n\n　またこの学校は卒業後の進路も多様とのこと。\n\n\n\n　ダンジョン関連はホットな分野で市場規模は大きく研究開発も盛んだ。例えばこの世界の発電所は過半数が魔石を使ったもので、エネルギー産業の多くがダンジョン資源に支えられているともいえる。この魔石発電は二酸化炭素を出さない上にコストも火力発電より安く、しかも小型化できるためかなり普及しているようだ。\n\n\n\n　他にもダンジョンから取れる素材を利用した素材技術革新も相当なもので、軍需産業やＩＴ産業も多大な恩恵を受けている。これらはとにかく富を生み、世界中が競って投資し研究開発を行っている。そのための優秀なダンジョン探索員は官民問わず多くの機関が喉から手が出るほど欲していて、冒険者学校には好待遇で青田買い目的のスカウトが来るそうだ。\n\n　\n\n　もちろん普通の大学へ進学することもできる。この冒険者学校の偏差値は相当に高く、去年の卒業生の進学先も錚々そうそうたる大学名が並んでいる。\n\n\n\n　そして成績について。\n\n\n\n「ここでいう成績というのは主に勉学とダンジョン攻略での成績の二つ。校内での試合やイベント、大会なども成績に加算されるが、それはまた後の機会に説明する」\n\n\n\n　ただダンジョン内でのみ活躍できればいい、というわけではなく、学業も成績に考慮されている。学力はダンジョンという未知の環境に対する適応力を高め、ステータスのＩＮＴ上昇にも影響が出るから重視されているそうだ。一応俺は元の世界で二流とはいえ大学は出ているし、学力勝負というならちょっとは有利かね。\n\n\n\n「ダンジョン攻略は仲間と協力して進めるものだ。同時に君らは成績を競い合うライバルでもある。是非精進してもらいたい」\n\n\n\n　ダンジョン攻略はゲームのときでも基本的にソロより前衛後衛のバランスがいい職業で組んで潜ったほうが効率が良かった。例外として浅層ではソロのほうがいい場合もある。パーティーメンバーを見つけて組むか、ソロでひっそりと潜るか。それは後で考えるか。\n\n\n\n「それでは今から端末を配るので、名前を呼ばれたらここに来い」\n\n\n\n　腕にはめてボタンを押すと目の前に映像が浮かぶ機能が付いたハイテクなウェアラブル端末だ。空中に文字などを表示する技術は元の世界でもあったが、ウェアラブル端末としてこれを実現できたことはないはず。これもダンジョンの恩恵を受けた技術の一端なのだろう。ガジェット好きのオラはワクワクが止まらないぜ。\n\n\n\n　早速、端末にあるボタンを押して開いてみると、目の前に１５インチほどの大きさの画面が開いた。他人の開いている画面も見えるので網膜に映しているのではなく、空中に投影しているタイプだ。\n\n　\n\n　トップ画面には名前やステータスが書かれている。\n\n\n\n\n\n＜名前＞　成海颯太ナルミ　ソウタ\n\n＜レベル＞　１\n\n＜ジョブ＆ジョブレベル＞ニュービー　レベル１\n\n＜冒険者階級＞：―未登録―\n\n\n\n＜ステータス＞\n\n最大ＨＰ：７\n\n最大ＭＰ：９\n\nＳＴＲ：３\n\nＩＮＴ：９\n\nＶＩＴ：４\n\nＡＧＩ：５\n\nＭＮＤ：１１\n\n\n\n＜スキル　１／２＞\n\n・大食漢\n\n・＜空＞\n\n\n\n\n\n　ふむ。ブタオの名前は成海颯太というのか……言われてみればそんな名前だったような。ともあれ、元の世界の俺はおっさんに片足突っ込んでたし、高校生活を送るうえで若返ってくれたのはポジティブな面だ。\n\n\n\n　レベルとジョブレベル（※１）は共に１だ。戦ったことがないから１なのだろう。ちなみに【ニュービー】ってのは「初心者」や「新参者」とかいう意味で、初期状態なら例外を除いて最初のジョブは【ニュービー】となる。経験値を貯めてジョブレベルを上げていけば特定のスキルを覚えたり、他のジョブへジョブチェンジしたりすることもできる。\n\n\n\n　冒険者階級が未登録になっているのは、現時点では冒険者ギルドで登録をしていないからだろう。ダンジョンに入るなら早いところ、冒険者ギルドへ行ったほうがいいと心にメモしておく。\n\n\n\n（ステータスの能力値は……正直低いな）\n\n\n\n　ゲームではこの初期能力を決めるのに何度もリセットマラソン（※２）をしてＡＬＬ１０以上のステータスとレアスキルを狙ったものだ。育ってしまえば初期ステータスなんて誤差みたいなものになるが……まぁ文句を言っても変わる事は無いので気にしないでおこう。\n\n\n\n　これらの数値は入学試験のときのジョブチェンジ装置で測定した数値らしい。それが冒険者学校のデータベースに送られてこの端末に転送されたものなので、リアルタイムのステータスが反映されているわけではないということは注意しなければならない。\n\n\n\n　――そして。\n\n\n\n（……え？　《大食漢》なんてスキルは初めて見た。というかコレのせいで太ってるんじゃないのか？）\n\n\n\n　この世界ではダンジョンでレベルやジョブレベルを上げていなくても初期の状態からスキルを覚えている人もいる。攻撃スキルや回復魔法なんてのを覚えていると序盤におけるダンジョンダイブがスムーズになるため、俺もリセットマラソンをして良スキルを狙っていたものだが……《大食漢》なんてスキルが果たして何の役に立つのか。\n\n\n\n　文字からして大量に食べそうなスキルだけど……もしこの体で生きていくことを強いられるのならば、さっさと他のスキルで上書きしてダイエットに励んだほうが良いかもしれない。ダンジョンに潜るのに階段を上がるだけで息を切らしている場合ではないのだ。\n\n\n\n　他には電話やメール、カメラ、ＳＮＳ機能がある。ダンジョン内で仲間との通信にも使えるし、これで作戦指示や指揮も可能なようだ。レポート提出などにも使う機能もある。\n\n\n\n（さて、肝心のログアウトの項目だが……ない。やっぱりないぞ。ログアウトできないのか？）\n\n\n\n　やはり意識だけがゲームの世界にあるのではなく、完全な転移なのだろうか。端末のインターフェースにログアウト項目がない以上、他に帰る手段は思いつかない。どうしても帰りたいというわけではないが、ブタオになってしまったせいで鬱々とした気分だ。\n\n　\n\n　せっかく夢にまで見た「ダンエク」の世界の中に来ることが出来たのに……\n\n\n\n（※１）レベルとジョブレベル\n\nレベルが上がるとステータスも上がり、恩恵を受けることができる。「ダンエク」での最大レベルは９０だった。\n\nジョブレベルは最大で１０まで。ジョブレベルを上げるとスキルを覚えることがある。ジョブチェンジするとジョブレベルは１からスタートとなる。ジョブによってはステータスにボーナスが加わるものもある。\n\n\n\n（※２）リセットマラソン\n\nゲームをリセットしニューゲームから再び始め、キャラを作り直して良いボーナス値のステータスや特典を狙う方法。略して「リセマラ」とも言う。"
                    },
                    {
                        "text": "臺版中文翻譯、潤色、校對結果: 第2話　成海飒太\n\n　選擇「隨機角色」之後就變成「肥豬」。\n\n \n\n　直到剛才我還覺得「難得都來到遊戲世界了，不就可以壹邊裝逼，壹邊跟女主打情罵俏不是嗎」，對于這樣的學校生活還抱有淡淡的期待，可如今已經徹底粉碎了。\n\n \n\n　鏡子中映照出的男高中生有壹米七左右的身高，發型是深藍色的大背頭。然而在那似乎可以輕易突破100公斤重的肥胖身軀中，脖子都被遮掩得看不見。明明不是天氣較熱的日子，可爬壹下樓梯就已經滿身大汗，還氣喘籲籲。\n\n \n\n「這……真的是我嗎？」\n\n \n\n　鏡子中的男人似乎也感到驚訝地望著這邊。簡直就像是在模仿著自己壹樣。看到對面的樣子，差點都要失去意識，很想逃避現實。\n\n \n\n　由于在原本的世界當中我也是標准的體重，從來沒有發胖過，所以幾乎沒有經曆過爬樓梯再走幾步就氣喘籲籲的經驗。也許這只是整人的――雖然也不可能是整人的――但我還嘗試做壹些奇妙的表情，擺出各種姿勢，可鏡子裏的男人怎麽看都是我自己……\n\n \n\n「嗚喔喔……我就不應該選擇隨機角色的……」\n\n \n\n　我抱著頭蹲下，可突出的肚子擋住我了。\n\n \n\n　我還以爲「隨機角色」是制作出隨機能力與隨機外表的功能，沒想到居然是從既有的角色當中選擇。明明E班有壹大堆長相不錯的角色，偏偏卻給我選到肥豬，運氣真是糟透了。\n\n \n\n　肥豬是進入某個女角色的個人線之後就出場的惡役角色。\n\n \n\n　每次都說些龌龊的話騷擾女角色，面對關系與她越來越好的男主也是壹直搞事情。最終被主角逼到退學，然後再攻略完成就可以達成幸福結局。我回想起這整壹個流程。\n\n \n\n　話是這麽說，肥豬倒也不是主角的競爭對手。強也不強，只不過是讓人惡心而又礙事的路人而已，所以我也沒有多少印象。在遊戲裏面也是叫\"肥豬\"，他的本名是什麽我也不知道。\n\n \n\n「說起來肥豬跟那位女角色……早濑華夜好像是他的青梅竹馬，而且還是未婚妻」\n\n \n\n(飒:由于設定集以及作品都是片假名，所以名字只能從網上找到類似讀音的漢字代替，也就是華夜)\n\n \n\n　我回想起關于早濑華夜的信息。\n\n \n\n　她是壹位日式和風的女孩子，四肢纖細，睫毛細長，鳳眸雙眼的四肢，還有壹頭長及腰部的馬尾。初中還有過在劍道的全國大會上取得優勝的經驗，學習也不差，正所謂文武雙全。性格直爽，面對誰都可以平等對待――除了肥豬。\n\n \n\n　主線進行到壹定程度，早濑華夜就會成爲男主強而有力的搭檔，也可以成爲戀人。不過站在肥豬的立場看來，他應該無法忍受自己喜歡的青梅竹馬，而且還是未婚妻這麽簡單地就被爽朗的男主搶走吧。雖然反擊方式是性騷擾也是沒救了就是了。\n\n \n\n　問題是在入學的時機點上――很悲哀的是肥豬――也就是我跟她的關系已經是非常惡劣。雖然不知道在這邊的世界是否壹樣討厭我，不過還是盡量少接近她吧，以免産生糾紛。\n\n \n\n　――話說真奇怪。\n\n \n\n　越是想著早濑華夜的事情就越覺得焦慮。難道說心中某處還留有肥豬的記憶或者情感嗎……。總感覺好像要想起什麽事情，但又好像遇到什麽障礙總是想不出來，真讓人煩躁。\n\n \n\n　再繼續想下去也只會因爲焦慮而煩。還是回到教室吧。\n\n \n\n　不知是第幾次深深地歎氣之後，我走進了教室。馬上就感覺到剛才提到的女角色那尖銳的視線。這時候還是裝作沒看見好了。\n\n \n\n（在這個時間點上她就已經非常討厭我了）\n\n \n\n　從肥豬的記憶裏面也回憶不起任何信息，關系惡劣成這樣的原因以及解決方法也都不知道。只能期待時間可以解決壹切。\n\n \n\n　重振精神尋找我自己的座位。位置好像是按照成績的順序從前面排到後面，而我的位置居然是最後面的”年級最差”地方……。我回憶壹下，入學考試是什麽樣子來著。‍‍‌‍‌‌‍‌‍‌‍‌‌‍‌‌‍‍\n\n \n\n　這座冒險者高中學校從A班到D班都是由冒險者初中部晉升過來的，也就是所謂的保送生，是國家特別選拔出來具有探索迷宮能力的學生。\n\n \n\n　另壹方面，只有Ｅ班是外部考試。錄取率爲百分之壹以下，能錄取的都是相當厲害的精英。記得好像是這樣的設定。\n\n \n\n　既然肥豬可以進來這座學校，那肯定是通過那魔鬼般的錄取率。是有什麽特殊的技能嗎？　即便是年級最差，能錄取也很厲害了，應該是有自信的吧。\n\n \n\n　班級裏面似乎有幾個人是認識的，彼此在聊著天。不過也許是因爲緊張的緣故，整個教室的氛圍十分僵硬。男主和女角色也是極爲安分，顯得純真可愛。\n\n \n\n　在我發著呆望著這群同學的時候，壹位年齡大概二十多歲左右，身穿西裝的年輕男子走進了教室。\n\n \n\n「各位同學，回到自己的座位上。接下來開始主持早會。首先是介紹壹下我自己以及這座學校，然後再向大家說明壹下成績和畢業相關的事項」\n\n \n\n　據他的自我介紹，他是班主任，名字是村井壹。冒險者大學畢業。也就是說他也是在這座冒險者高校以優秀成績畢業的OB吧。雖然體格不是很強壯，不過從言行舉止以及身法來看，應該不是普通人。與其說是學校的老師，不如說更像是軍人。在這壹年裏是由這位老師來指導我們。\n\n \n\n　老師介紹完自己之後，在白色黑板上逐行寫上關于學校的信息。\n\n \n\n「在這座學校中只要取得不錯的成績就可以獲得國立冒險者大學的推薦名額，又或者是成爲冒險者的時候可以享有優待政策。壹流的氏族和民間企業也都會來招收聘請。而這些主流的出路基本上都是根據成績排名分配的」\n\n \n\n　國立冒險者大學是壹所主要以迷宮相關的專業特殊部隊，以及迷宮省的預備官員爲培養目標的大學。用原來的世界來說，比較接近于防衛大學和氣象大學。據老師所說，晉升冒險者大學是最受歡迎的出路。\n\n \n\n　其次是優待政策。\n\n \n\n　這所學校的學生都可以享受類似于公務員壹樣的各種優待，比如冒險者公會裏面設施的使用費用減半，以及壹部分設施可以免費利用。就跟日本國公立大學的學生那壹丁點優待很相似。在利用設施時需要注意是否要提前申請。\n\n \n\n　還有冒險者學校的學生的冒險者階級（分爲１～１０級，１級最高10級最低）是從9級開始，通過簡單的手續就可以獲取進入迷宮的資格。而普通人在經過手續之後，還要提供身份證明、通過筆試、聽完講習、經過實地訓練之後才能從10級開始，相當麻煩。\n\n \n\n　冒險者公會的委托接受是受到冒險者階級限制的，壹定的等級之上還可以享受國家的優待政策。提升冒險者階級只有好處沒有壞處，所以希望學生們都要銘記于心，熟悉委托並參加升級考試。\n\n \n\n　還有這所學校的出路有不少。\n\n \n\n　迷宮相關的都是熱門專業，市場規模不小，研究開發也是十分活躍。比如說這世界的發電所多半都是使用魔石，所以也可以說是迷宮支撐著能源産業的大半。魔石發電不僅不會産生二氧化碳，而且消耗速率比起火力發電還要低，並且由于可以小型化搭建，如今似乎相當普及的樣子。\n\n \n\n　其他還有從迷宮中獲取到的素材進行利用，産生相當大的素材技術革新，軍需産業和IT産業都獲得不少的恩惠。總之這些都促進了經濟，全世界都在競爭著投資研發。因此優秀的迷宮探索者，無論是否官員也是許多機構求之不得的人才，似乎還會來到冒險者學校以不錯的待遇來提前招聘。\n\n \n\n　當然，學生也可以選擇普通的大學。這所冒險者學校的偏差值相當高，去年畢業生的出路也都是名牌大學。\n\n \n\n　而關于成績方面。\n\n \n\n「這裏的成績主要分爲學習和迷宮攻略的成績。校內的比賽、活動、大會雖然也會加在成績之中，不過這些等下次有機會再說」\n\n \n\n　不是只要在迷宮內有所成就就行，學習也是包括在成績之內。學力可以提高對待迷宮這種陌生環境的適應能力，而且還會影響到狀態數值中的ＩＮＴ，因此似乎十分受到重視。姑且我在原本的世界也是上過大學，雖然是二流大學，但在學力競技上還是有點優勢的。\n\n \n\n「迷宮攻略是需要與同伴齊心協力的。同時妳們也是在成績上的競爭對手。還請務必精進自己」\n\n \n\n　在遊戲中迷宮攻略的效率比起單刷，還不如前衛後衛搭配合適職業要來得快。除了在底層單刷是例外。我是要找人組隊呢，還是壹個人偷偷單刷呢。這件事待會再考慮吧。\n\n \n\n「那麽現在開始分發設備，叫到名字的來這裏」\n\n \n\n　戴在手腕按下按鈕後就會眼前浮現出窗口的高科技設備。雖然原本的世界也有在空中浮現出文字的技術，不過應該沒有實用到隨身攜帶的程度。這應該也是受到迷宮的恩惠新開發的技術之壹吧。這種高科技的氛圍真是讓人興奮不已。\n\n \n\n　我馬上就嘗試按下設備上的按鈕，隨後眼前出現十五公分大的窗口。其他人打開的窗口我也可以看得見，類型應該是投影至半空中，而不是當事人的視網膜。‍‍‌‍‌‌‍‌‍‌‍‌‌‍‌‌‍‍\n\n \n\n　窗口頂端顯示著名字和狀態數值。\n\n \n\n＜名字＞　成海飒太（ナ兒ミ　ソウタ）\n\n＜等級＞　１\n\n＜職業＆職業等級＞Newbie　等級１\n\n＜冒險者階級＞：―未登陸―\n\n＜狀態數值＞\n\n \n\n最大ＨＰ：７\n\n最大ＭＰ：９\n\nＳＴＲ：３\n\nＩＮＴ：９\n\nＶＩＴ：４\n\nＡＧＩ：５\n\nＭＮＤ：１１\n\n＜スキ兒　１／２＞\n\n・大食漢\n\n・＜空＞\n\n \n\n　嗯，肥豬的名字是叫成海飒太嗎……想了想好像是這名字來著。不管怎麽樣，原本的世界我都差不多是大叔了，不僅可以體驗高中生活，還讓我變得更年輕，也沒多少負面想法。\n\n \n\n　等級和職業等級（※１）都是1。畢竟沒有戰鬥過，所以是1吧。順便壹提，【Newbie】是「新手」和「新人」的意思，初期狀態除了特殊情況以外都是【Newbie】。經驗增加提升職業等級就可以學習特定的技能，並且還可以轉職爲其他的職業。\n\n \n\n　冒險者階級之所以是未登錄的狀態，應該是因爲我還沒有在冒險者公會登記過吧。如果要進入迷宮還是早點到冒險者公會那邊比較好，我將這件事記在心中。\n\n \n\n（狀態數值……老實說很低）\n\n \n\n　在遊戲中都是用刷初始號（※２）的方式得到全屬性10以上以及稀有的技能。雖說真要培養起來，初期的數值就跟誤差沒兩樣就是了……嘛啊，抱怨也是無濟于事，還是不要在意了。\n\n \n\n　這些數值似乎都是入學考試的時候利用職業轉職裝置測定的。然後傳送到冒險者學校的數據庫之後再傳回到這個設備上，因此需要注意的是這些數值並不是最新的數值。\n\n \n\n　――最後。\n\n \n\n（……咦？我還是第壹次看見《大食漢》這個技能。是說該不會是因爲這玩意才會發胖的吧？）\n\n \n\n　這世界有些人即便不用在迷宮中提升等級和職業等級，初期狀態也會擁有技能。如果前期就學會攻擊技能或者回複技能就不會卡進度，所以我當初也是刷初始號選擇有這些技能的……《大食漢》這個技能究竟有什麽作用呢。\n\n \n\n　從字面意思來看好像是大吃大喝的技能……如果真的要用這身體活下去，也許還是趕緊用其他技能替換掉它，然後開始減肥比較好。現在可由不得我攻略迷宮時爬爬樓梯就累得不行。\n\n \n\n　其他還有電話、短信、照相機、ＳＮＳ功能。還可以在迷宮裏面與同伴聯系，這樣就可以指揮作戰。並且還有提交報告時可以利用到的功能。\n\n \n\n（好了，最重要的退出選項……沒有。果然沒有耶。不能退出嗎？）\n\n　果然不是只有意識轉移到遊戲世界，也許是徹徹底底的轉移。設備上的界面沒有退出選項，我也想不到其他可以回去的手段。倒也不是說我很想回去，只是因爲自己成爲肥豬，心情有些郁悶而已。\n\n　明明都來到夢寐以求的「地探史」的世界當中……\n\n\n \n\n（※１）等級與職業等級\n\n \n\n等級提升之後，狀態數值也會提升，還可以享受壹些好處。在「地探史」中等級上限爲90。\n\n職業等級最大爲10。職業等級提升之後可以學會技能。轉載之後職業等級會從1級開始。根據職業的不同，狀態數值會有額外的加成。\n\n（※２）刷初始號\n\n壹種通過重置遊戲後開始新的遊戲來決定自己新建角色的數值高低與擁有特典的方法。簡稱「刷初始」。"
                    },
                    {
                        "text": "日文輕小說原文: " + content
                    },
                    {
                        "text": "臺版中文翻譯、潤色、校對結果: "
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": temperature,
            "topK": topK,
            "topP": topP,
            "maxOutputTokens": 30720,
            "stopSequences": []
        },
        "safetySettings": [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=timeout)
    except Exception as e:
        return {'error': str(e)}

    return response.json()

def memo_api(API_KEY, content, timeout=60):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"


    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "請你根據文章日文原文，把其中所有的名字、特殊名詞 、店名、技能名、片假名字翻譯成繁體中文並總結成日中對照形式如範例所示格式。不要列出句子、不要列出未在原文中出現的詞語、不要列出普通名詞。"
                    },
                    {
                        "text": "日文原文: 第3-22話　氷雪公女①\n『第六階位が1人。氷雪公女の前であるぞッ！！』\n\n氷雪公女の威嚇（いかく）するような名乗り上げ。\nそれと同時に、さっきまでの夏のむっとした空気は完全に消え去って冬の凍えるような風が吹き荒れた。\n\n俺は『導糸（シルベイト）』を繭みたいに広げて、冬風から自分たちを守る。"
                    },
                    {
                        "text": "特殊名詞日中對照表: | 日文原文 | 繁體中文 |\n|---|---|\n| 氷雪公女 | 冰雪公主 |\n| 導糸 | 導絲 |"
                    },
                    {
                        "text": "日文原文: 俺は『属性変化：水』と『風』を組み合わせて、空いっぱいに水を霧のように撒き散らした。すると、太陽の光がそれを反射して……。\n\n「虹！　にいちゃ！　虹がでた！」\n「キラキラしてるでしょ？」\n「うん！　きれい！！」\n\nこういう攻撃にならない魔法の練習は強くならないと思うが、俺の作った虹を見てきゃっきゃと騒ぐヒナを見ていると、たまにはこういうのを悪くないと思う。\n\nそれに、二重属性操作の練習になるしな。\n俺が自分で作った虹を見ていると、縁側に座っていたヒナが立ち上がると走ってこっちにやってきた。\n\n\n3歳の言葉は時々わからないので、俺は首をかしげた。\n「ヒナ、気をつけるのよ」"
                    },
                    {
                        "text": "特殊名詞日中對照表: | 日文原文 | 繁體中文 |\n|---|---|\n| 属性変化：水 | 屬性變化：水 |\n| 二重属性操作 | 二重屬性操作 | \n| ヒナ | 雛 |"
                    },
                    {
                        "text": "日文原文: 第2-17話　来客ヌーブ\nニーナちゃんに誘われて、マンションに備え付けられているエレベーター（めっちゃ綺麗）に乗りながら、俺は自分が本当に小学生だったときのことを思い出していた。"
                    },
                    {
                        "text": "特殊名詞日中對照表: | 日文原文 | 繁體中文 |\n|---|---|\n| ニーナ | 妮娜 | \n| エレベーター | 電梯 |"
                    },
                    {
                        "text": "日文原文: 第1話　「俺たちは、最高の仲間だ」\n俺の名前はアーロン・ゲイル。１５歳。\n世界最大の迷宮を擁する、世界最大の都市【神骸都市ネクロニア】で、迷宮探索者として働く一人だ。"
                    },
                    {
                        "text": "特殊名詞日中對照表: | 日文原文 | 繁體中文 |\n|---|---|\n| アーロン・ゲイル | 亞倫·蓋爾 |\n| 神骸都市ネクロニア | 神骸都市涅克羅尼亞 |"
                    },
                    {
                        "text": "日文原文: 第三話　滾る野心\n「それで。意識を取り戻したという報告は聞いていたけれど。最近の呪い人形の様子を詳しく教えてもらえるかしら」\n「は、はい。ギルモア様はそれはもう毎日お幸せそうです。玩具を買いそろえるばかりでなく、つい先日も新しいドレスを新調なさいました。後は、絵師を呼び出して、親子の永遠の記録とすると仰られて」\n「あ、そう。実に馬鹿馬鹿しいわね。そんなものを書き残したところでゴミにしかならないでしょうに。お前もそう思うでしょう？」\n「は、はい」\n「それにしても忌々しいわ。不愉快極まりない」\n\nここはブルーローズ家別館。ギルモアの後妻であるミリアーネは、執事ピエールから報告を聞いて心底苦々しい顔をしていた。あの呪い人形が復活してから一ヶ月。――魔光石と子供の死骸から採取した触媒をブレンドした秘薬とやらを、約10年もの間投与されつづけてきた呪い人形だ。その顔はあの女――前妻ツバキに瓜二つ。その上、使用人たちの話ではまるで悪魔のような表情で笑うのだとか。悪評が広まるのも時間の問題だ。そんなことでブルーローズの名に泥を塗られてはたまったものではない。さっさと死なせてしまえば良かったものを。\n\n「本当に救えないわね。金は減る一方なのに、本人にはまるで自覚なし。当主の資格があるのかしら？」\n「…………」\n「黙っているけど。お前も他人ごとではないのよ？　破産したらどうやって食べていくのかしら」\n「し、しかし私どもにできることなど」\n「まぁ期待などしてないけどね、愚痴ぐらい言いたくなるものよ」\n\n一体あの男は、どれだけの財産を浪費すれば気が済むのか。ブルーローズ家所有の芸術品、武具などはかなりの数が既に売り払われている。挙句の果てには、土地にまで手をつけようとする始末。これはミリアーネが裏で手を回して即座に握りつぶした。いずれこの土地は息子グリエルが継承するのだ。芸術品などはどうでもよいが、土地だけは絶対に許さない。貴族の誇りにして魂である。売り渡すなどありえない。\n\n「とっとと後を追って死ねば良かったのよ。愚かなほど長生きするというのは本当なのかしら。羨ましい限りね」\n\nピエールから差し出された報告書をビリビリと破くと、ぽいっと投げ捨てる。慌てて拾い集めるピエール。ピエールは外見だけみると誠実かつ忠誠心に篤そうに見えるが、中身と一致していない。保身が第一であり、ギルモアへの忠誠心はないと言っていい。現に逼迫していく資産を見てミリアーネ側に簡単についた。こいつだけではない、使用人の全てをミリアーネは引き込んでいる。報酬は、現在の給金とギルモア死後も引き続き雇用を続けるという保証だけ。これだけで、ギルモア周囲の情報が全て入ってくる。\n\n「さぁて、どうしようかしら」\n\nイエローローズの家から政略結婚で嫁いだ身。二人の男子を儲けたことで十分にその役目は果たしている。ギルモアの役目ももう終わっている。後はとっとと引退、もしくは病死してくれれば全てが上手くいく。イエローローズ家は国王に近しい家、当然議会でも王党派の筆頭だ。中立を保つブルーローズ家を引き込む事ができれば、イエローローズ家にとって都合の良い政治が行なわれることになる。国王ルロイとの水面下での折衝も、父が終わらせている。ブルーローズの家を継ぐのはグリエルと報告済みだ。ギルモアがどれだけ抵抗しようと、ミツバなどという呪い人形がその座につく事は絶対にない。\n\n「奥様、一つ悪い知らせがございます」\n「あらあら、なにかしら。怖いわねぇ」\n「青薔薇の杖の継承を、ギルモア様は既に行なわれたようです。杖の所有権は、その、ミツバお嬢様に。今ではお嬢様が常に持ち歩いていらっしゃいます」\n「まぁ、それは大変。でも、そんな勝手なことをして、自分がどうなるか考えていなかったのかしらねぇ」\n\nミリアーネは薄く笑う。由緒ある七杖家継承者の証である、各色の薔薇の杖。その杖は継承の儀式を行わなければ、握ることすらできない。薔薇の杖は持ち主を選ぶのだ。資質のないものが無理に握ろうとすれば死の代償を得ると伝わっている。ギルモアはその杖を死守することで、自分が当主であり、後継者を選ぶのも自分であると広言していた。\n\n（余計な仕事を増やしてくれて。本当に面倒なことばかりしてくれるわね）\n\nだが、特に問題はない。杖が本物であろうとレプリカであろうと誰も気にしない。当主自ら先頭に立って戦場にでることはもうないのだ。ここ二十年で戦争は大きく様相を変えたから。だから、本物の杖を誰が持っていようが気にしない。ブルーローズの家に存在しているだけで良い。\nミリアーネが、ギルモアの浪費に目を瞑っていたのは穏健に家督継承を済ませたかったからに過ぎない。医者が言うには、酒に溺れていたギルモアの内臓はボロボロとのこと。麻薬と言い換えることの出来る鎮痛剤を毎日飲んでいることも知っている。他にも重い病を患っている可能性も高い。だから見逃してきた。だが、それももう終わりだ。杖もなく、ひたすら財産を食いつぶす害虫。当主としての役割を何一つ行なうこともせず、呪い人形にかまけてきた哀れな男。そんな男の妻とされた自分も十分哀れだろうが、ブルーローズ家乗っ取りには成功した。何ら恥じることはない。\n\n「……奥様？」\n「ああ、少し考え事をしていたわ。……さて、お前の報告によると、来月お披露目のパーティを計画しているのだったかしら」\n「は、はい」\n「ふん。あの男、恐らくそこでミツバに家督継承を発表する気でしょうね。ふふふ、それはそれで面白いかしら。ならば、そこで決着をつけましょう」\n「け、決着ですか」\n「ええ。グリエルとミゲルは忙しいでしょうし、後で色々言われるのは可哀相だから欠席させましょう。いつものように、私が全部掃除しなくてはね」\n\nいずれにせよ、事を行えば多かれ少なかれ悪い噂は流れる。ギルモアの今までの所業を利用して、自業自得という風に揉みつぶしていくつもりだが。くだらぬ悪評は母である自分が背負えば良いだろう。グリエルは立派な当主として、ミゲルには上院議員として立派に働いてもらいたい。そうすれば自分も報われるというもの。\n\n「は、はい」\n\n「さてピエール。あとであるモノを渡すから、それをあの男のグラスに仕込みなさい。臨時報酬は百万ベルよ。大変な仕事だけど、やってみたいかしら？」\n「……それは、ま、まさか」\n「ええ、そうよ。これはお前の忠誠心を試すためのテストでもあるの。勿論断ってもいいわよ。罪深い行為であることには違いないし。どちらにせよ、お前がしくじった場合に備えて、手の者を数人客として紛れ込ませるから心配は無用、結末は一切合切何も変わらない」\n\nそう言って笑うと、ピエールは暫し悩んだ後、跪いて頷いた。\n\n「聞き分けが良くて助かるわ。色々あったけど、最後には全て上手く行きそうねぇ。後はあの呪い人形をどうするか、かしら。一緒に始末できれば良いのだけど、なにせあの女が目をかけているからねぇ」\n\nミリアーネは髪を弄りながら、しばし思考する。ギルモアは確実に殺す。ついでにミツバも殺してしまいたい。だが、あれは王国魔術研究所が関与してしまっている。植物状態だったあれを無理矢理生存させてきた頭のおかしい連中だ。生贄の実験動物ではなく、魔術の観察対象としてみていた場合、後で揉めるはめになる。特に所長のニコレイナスと敵対するのは避けたい。あの女は近代の戦争のあり方を変え、王国躍進の一翼を担った天才。敵対よりは協調していったほうが得策だ。\n\n「それとなく聞いてみるとしましょうか。ピエール、ニコレイナス所長に使いを出しなさい。娘のことで早急にお会いしたいとね」\n「かしこまりました」\n\nピエールが下がった後、机をトントンと叩いて命令する。前には誰もいないが、背後に複数の気配を感じる。\n\n「呪い人形の悪評をばら撒きなさい。死体の血を啜って蘇った化け物、母親を殺し、次は父親を呪い殺そうとしていると。後はギルモアの体調が急激に悪くなっているともね」\n\nどうせ悪評は広まるのだ。ならば先手をうって操作してしまった方が良い。こちらには非が及ばないように浸透させる。\n\n「…………対象地域は？」\n「ブルーローズ州だけでなく、王都周辺にもよろしく。あそこに撒いておけば、ローゼリア全土に風評として流れる事でしょう。金はイエローローズの父に請求しなさいな。そっちの利益も大きいのだから、嫌とは言わせないわ」\n「承知しました」\n\n背後から気配が消える。いわゆる子飼いの密偵だ。イエローローズから連れてきた連中。荒事からこういった裏工作までお手のもの。これで、来月のお披露目会までには愉快な風聞に塗れている事だろう。ギルモアはどんな顔をしてそれを聞く事になるのだろうか。実に楽しみなことである。ミリアーネは楽しそうに笑った。\n\n「黄と緑に青が加わる。王党派内での勢いを増せば、私たちは更に栄える事ができる。国王も私たちの勢いを無視出来ないわ。まさに、ローゼリア万歳、議会政治万歳ってとこかしら」\n\n国軍結成による私兵所有の大幅制限。その代わりに受け入れさせた議会制。一時はどうなるかと思ったが、貴族の世はどうやら終わらないようだ。ローゼリアは大陸有数の強国となり、王権は制限され、貴族の力は更に強まっている。いずれは、自分も議員とやらになるのも悪くないかもしれない。可能性は十分にある。ミリアーネは湧き上がってくる大量の野心に、思うがまま身を委ねることにした。"
                    },
                    {
                        "text": "特殊名詞日中對照表: | 日文原文 | 繁體中文 |\n|---|---|\n| ブルーローズ | 藍薔薇 |\n| ミリアーネ | 米莉安妮 |\n| ピエール | 皮耶爾 |\n| ギルモア | 吉爾摩 |\n| ツバキ | 山茶花 |\n| グリエル | 格里爾 |\n| ミゲル | 米格爾 |\n| イエローローズ家 | 黃薔薇家 |\n| ルロイ | 勒洛伊 |\n| ミツバ | 三葉 |\n| ニコレイナス | 尼可雷納斯 |\n| ローゼリア | 羅瑟莉亞 |"
                    },
                    {
                        "text": "日文原文: " + content
                    },
                    {
                        "text": "特殊名詞日中對照表: "
                    }
                ]
           }
          ],
          "generationConfig": {
            "temperature": 0.1,
            "topK": 1,
            "topP": 0.1,
            "maxOutputTokens": 30720,
            "stopSequences": []
          },
          "safetySettings": [
            {
              "category": "HARM_CATEGORY_HARASSMENT",
              "threshold": "BLOCK_NONE"
            },
            {
              "category": "HARM_CATEGORY_HATE_SPEECH",
              "threshold": "BLOCK_NONE"
            },
            {
              "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
              "threshold": "BLOCK_NONE"
            },
            {
              "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
              "threshold": "BLOCK_NONE"
            }
          ]
        }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=timeout)
    except Exception as e:
        return {'error': str(e)}

    return response.json()






