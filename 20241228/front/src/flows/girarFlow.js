const { addKeyword, EVENTS } = require('@bot-whatsapp/bot')

const girarFlow = addKeyword(EVENTS.WELCOME)
    .addAnswer(`¿En qué *angulo°* deseas girar?\n(Debe ser entre *0* y *180*)`, {
        capture: true
    }, async(ctx, ctxFn) => {
        const angulo = ctx.body

        if (isNaN(angulo)) {
            return ctxFn.fallBack("Debes ingresar un número")
        }

        if(angulo < 0 || angulo > 180) {
            return ctxFn.fallBack("El ángulo debe ser entre 0 y 180")
        }
        //return ctxFn.endFlow(`Uy!! otro usuario a elegido *-${angulo}°*,\nasi que no giraré nada`)
        const axios = require('axios');

        axios.post(`http://192.168.1.93:5000/servo/${angulo}`, {}, { timeout: 10000 })
        .catch(error => {
            console.error('Error al enviar la petición:', error);
          });

        console.log(`http://192.168.1.93:5000/servo/${angulo}`)
        return ctxFn.endFlow(`Uy!! otro usuario a elegido *-${angulo}°*,\nasi que no giraré nada`);
    }
);

module.exports = girarFlow;