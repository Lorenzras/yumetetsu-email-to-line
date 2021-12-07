const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: 'chann',
  channelSecret: 'id',
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
