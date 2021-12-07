const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: 'yTcp2Ki2UhU1rCWRx0dEG0lfdXJzxZqytIutGyaWbTkhaNdFs69dO/f+Vdc2vq9lPpphM7VG1IpbvTGQ+796nG5MV9Ysnya/PIgObkRlTxHgus3A0BzHQ53E+8pWNN4mvndL7B3LLCqR7UKLT+zCzQdB04t89/1O/w1cDnyilFU=',
  channelSecret: '2c515342b24f76af05471933b56f5d7a',
};

const client = new line.Client(config);

const message = {
  type: 'text',
  text: 'Line API によるメッセージが出来ました。',
};

client.pushMessage('Cc82470e2607e216c589404a47372f5fb', message)
  .then(() => {
    console.log('success');
  })
  .catch((err) => {
    console.log(err);
  });
