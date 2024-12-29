const { addKeyword, EVENTS } = require('@bot-whatsapp/bot')
const axios = require('axios');

const tamarindoFlow = addKeyword(EVENTS.WELCOME)
    .addAction(async(ctx, ctxFn) => {
        try {
            const response = await axios.get(`http://192.168.1.93:5000/tamarindo`);
            console.log('Respuesta:', response.data);
            return ctxFn.flowDynamic(response.data);
        } catch (error) {
            console.error('Error al enviar la petición:', error);
            return ctxFn.flowDynamic('Hubo un error al procesar tu solicitud');
        }
    });

module.exports = tamarindoFlow;