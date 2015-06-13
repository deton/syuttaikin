# 出退勤表示機

会社で使われている在・不在スライド付きの名札掛を、
出勤時と退勤時に手で操作するのが面倒になったのと、たまに操作するのを忘れるので、
自席PCの電源のオンオフに合わせて青と赤の表示を切り替えるものを作りました。

目的は、[出退表示LED](https://github.com/deton/presenceled)と同じです。
LED点滅表示だと、ぱっと見た時にわかりにくいので作成。

![画像](../img/syuttaikin.jpg)

## 構成

```
    自席PC      server     LininoOne+servo
   (cron---->定期通知CGI)
                CGI<-------cron定期取得+サーボ制御
```

## 部品
### ソフトウェア
* LininoOS (`linup latest master`)
 * syuttaikin.py。MCU側に自席PCがオンラインかどうかを指示。cronで5分間隔で実行。
 * syuttaikin.ino。オンラインかどうかに応じてサーボ角度を制御。
* syuttaikin.cgi。サーバ上で動かすCGIスクリプト。
  自席PCがオンラインかどうかを返す。

### ハードウェア
* [Linino ONE](http://akizukidenshi.com/catalog/g/gM-08902/)。
  Linux+Arduino。Arduino Yunの小型版。
  Wi-Fi接続できてArduinoスケッチが使えて小型。
* 小型サーボモータ
* ピンヘッダ6本
* はさみで切れるユニバーサル基板
