<script setup lang="ts">
import { onMounted, ref } from 'vue'
import QRCode from 'qrcode'
import { RouterLink } from 'vue-router'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

const qrData = ref<HTMLCanvasElement | null>(null)

onMounted(() => {
  if (qrData.value) {
    QRCode.toCanvas(qrData.value, 'https://zosiuc.dev', {
      width: 180,
      color: {
        dark: '#46545f', // donkerblauw
        light: '#F4F4F4'
      }
    }, (error) => {
      if (error) console.error(error)
    })
  }
})

</script>

<template class="">
  <section class="flex flex-col w-[100vw] min-h-lvh pt-40 pb-20 items-center   text-center bg-gradient-to-b from-blue-200 via-white to-blue-50">
    <!-- Hero section -->
    <h1 class="text-4xl md:text-6xl font-bold text-gray-800 mb-4">
      {{t('welcome')}} <span class="text-blue-500">ZosG</span>
    </h1>
    <p class="max-w-2xl text-lg md:text-xl text-gray-600 mb-8">
      {{t('hero-p')}}
    </p>

    <!-- QR voorbeeld -->
    <div class="flex flex-col items-center bg-white shadow-lg rounded-xl p-6 mb-8">
      <h2 class="text-lg font-semibold mb-2">{{t('scan-qr')}}</h2>
      <canvas ref="qrData" class="rounded-xl"></canvas>
    </div>

    <!-- Call to action -->
    <RouterLink
        to="/qr"
        class="bg-blue-400 hover:bg-gray-200 text-white hover:text-blue-800 px-6 py-3 active:scale-75 rounded-lg text-lg font-semibold transition-all"
    >
      {{t('try-qr')}}
    </RouterLink>

    <!-- Features -->
    <div class="mt-16 grid gap-8 md:grid-cols-3 w-full max-w-5xl">
      <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-2">{{t('Quick&Easy')}}</h2>
        <p class="text-gray-600">{{t('Quick&Easy-p')}}</p>
      </div>
      <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-2">{{t('LogoIntegration')}}</h2>
        <p class="text-gray-600">{{t('LogoIntegration-p')}}</p>
      </div>
      <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-xl font-semibold mb-2">{{t('free')}}</h2>
        <p class="text-gray-600">{{t('free-p')}}</p>
      </div>
    </div>
  </section>
</template>
