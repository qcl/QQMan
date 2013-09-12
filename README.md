泛用型電子布告欄閱讀系統
--------
Software Design Patterns Final Project Report [pdf](http://qcl.github.io/QQMan/QQMan.pdf)

- B97501046 資訊四 李卿澄
- B98902018 資訊三 張偉哲

# QQMan

為了解決跨平台問題、提供安全連線機制、提供多樣解析 BBS 文本並令系統具有擴充能力，我們撰寫、設計了 QQMan 這個軟體。

QQMan 使用 Python 撰寫，並搭配使用 PyQt4（Qt 的 Python 實作版本）。由於使用 Python 撰寫，只要有 Python Interpreter 並同時搭配 PyQt4 的函式庫便能跨越多個平台運作，例如我們的開發便是同時使用 Linux 與 Windows 而完成的；使用 Python 開發無須編譯，這使得我們開發的速度大大的提升。

著名的 BBS 連線軟體 PCMan 最初是以微軟 MFC 撰寫，而後移植至 Linux 的移植版本 pcmanxgtk，由於 MFC 的 GUI 被限制在 Windows 平台，必須實作 Linux 上熱門的 Gtk+圖形介面，他們是以繼承原先 Windows 版本的 class，然後在原有架構下重新 has-a Gtk 的物件，觀察是一個Adapter pattern 的方法來完成 pcmanx-gtk，但是其結構已經完全被 Windows 版本限制住，擴充、修改上都受到了限制，甚至 code 在閱讀上小有障礙。

不同於 PCMan，我們的 QQMan 在結構設計階段是盡量跳脫了作業系統、顯示介面實作的限制，以期達到能夠在多作業系統、多圖形介面實作的方式運作（雖然目前我們只以 PyQt 實作，但可以擴充至以 PyGtk 等其他有 Python 實作版本的圖形介面）。我們將整個瀏覽 BBS 的過程拆成「連線」、「解析」、「（解析過後的）資料」、「（利用資料）顯示」四個部分、階段。是四個主要的類別群。

# Structure
* QQMan Classes
  * **QQMan** - 主程式
  * **QQManBuilder** - 依據參數產生 View 與 Socket 的 Builder
* QQMan 顯示 Classes
  * **QQManView** - Abstract view class
      * **QQManFrameView** - 利用 Qt Frame Widget 實作的顯示介面（畫圖顯示）
      * **QQManWebView** - 利用 Qt WebKit View 實作的顯示介面（顯示網頁）
* QQMan 資料 Classes
  * **QQManTerminal** - 儲存管理終端機的各種資訊
  * **QQManTermWord** - 終端機中的「字」
* QQMan 解析 Classes
  * **QQManParser** - Abstract parser class
      * **QQManBasicBig5Parser** - 實作了對 Big5 資料的基礎解析
          * **QQManBig5Parser** - 實作了對 Big5 資料的進一步解析
  * **ExtraBig5** - 擴增 big5 轉 unicode 表的 Abstract class
      * **ExtraBig5_0x8140_0xA0FE** - Big5 第一造字區轉 Unicode 表
      * **ExtraBig5_0xC6A1_0xC8FE** - Big5 第二造字區轉 Unicode 表
      * **ExtraBig5_0xF9D6_0xFEFE** - Big5 第三造字區轉 Unicode 表
      * **ExtraBig5_0xC940_0xF9D5** - Big5 次常用漢字區轉 Unicode 表
* QQMan 連線 Classes
  * **QQManConnect** - 連線功能的 Abstract class
      * **QQManTelnetConnect** - 利用 Qt telnet socket 實作的 telnet 連線
      * **QQManSslConnect** - 利用 Qt ssl socket 實作的 ssl 連線
