import { 
    defineConfig,
    presetAttributify,
    presetIcons,
    presetTypography,
    presetUno,
    presetWebFonts,
    transformerDirectives,
    transformerVariantGroup
} from 'unocss'

export default defineConfig({
    shortcuts: [
        
    ],
    theme :{
        colors: {
            windowBack: '#333',
        }
    },
    presets: [
        presetUno(),
        presetAttributify(),
        presetIcons(),
        presetTypography(),
        presetWebFonts({
            provider: 'google',
            fonts: {
                zen: [
                    {
                        name: 'Zen Maru Gothic',
                    },
                ],
            },
        }),
    ],

    transformers: [
        transformerDirectives(),
        transformerVariantGroup(),
    ],
})