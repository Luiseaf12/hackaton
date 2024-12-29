const { createBot, createProvider, createFlow, addKeyword, EVENTS } = require('@bot-whatsapp/bot')

const QRPortalWeb = require('@bot-whatsapp/portal')
const BaileysProvider = require('@bot-whatsapp/provider/baileys')
const MockAdapter = require('@bot-whatsapp/database/mock')

const girarFlow = require('./src/flows/girarFlow')
const tamarindoFlow = require('./src/flows/tamarindoFlow')

const fs = require('fs')
const path = require('path')

const menu = fs.readFileSync(path.join('./mensajes/menu.txt'), 'utf8')

const menuFlow = addKeyword(EVENTS.WELCOME)
    .addAnswer(menu)
    .addAction({ 
        capture: true }, 
        async(ctx, ctxFn) => {
            const opcion = ctx.body.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '')

            switch(true) {
                case opcion === '1':
                    return ctxFn.gotoFlow(girarFlow)
                case opcion === '2':
                    return ctxFn.gotoFlow(tamarindoFlow)
                case opcion === '99':
                    return ctxFn.endFlow("Saliste del menú")
                default:
                    return ctxFn.fallBack("Elige una opción válida")
            }
        }
    )

const main = async () => {
    const adapterDB = new MockAdapter()
    const adapterFlow = createFlow([
        menuFlow,
        girarFlow,
        tamarindoFlow,
    ])
    const adapterProvider = createProvider(BaileysProvider)

    createBot({
        flow: adapterFlow,
        provider: adapterProvider,
        database: adapterDB,
    })

    QRPortalWeb()
}

main()
