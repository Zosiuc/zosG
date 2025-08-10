<script setup lang="ts" >
import { useI18n } from 'vue-i18n'
import { watch } from 'vue'
const { t, locale } = useI18n()

import facebook from "/facebook.png"
import x from "/twitter.png"
import linkedIn from "/linkedin.png"
import whatsapp from "/whatsapp.png"
import email from "/mail.png"
import faceLogo from "/faceLogo.svg"

watch(locale, (newLocale) => {
  document.documentElement.dir = newLocale === 'ar' ? 'rtl' : 'ltr'
}, { immediate: true })

</script>
<template >

  <div class=" ">

    <nav class=" z-10 p-4 px-6 flex justify-between fixed top-0 left-0 w-full h-18 z-1000 bg-white/25 backdrop-blur-xl  gap-6">
      <div class="flex gap-6 items-center justify-center">
      <router-link to="/" class="text-gray-800 text-xl">{{t('home')}} |</router-link>
      <router-link to="/qr" class="text-gray-800  flex items-center">{{t('QR-generator')}}</router-link>

      </div>

      <div>
      <select v-model="locale" class="rounded-2xl bg-blue-400  text-xs h-8 text-white flex items-center">
        <option value="en" class="">{{t('english')}}</option>
        <option value="nl">{{t('dutch')}}</option>
        <option value="ar">{{t('arabic')}}</option>
      </select>
      </div>
    </nav>

    <router-view />

    <footer class="z-1000 bg-white/25 backdrop-blur-xl p-2  h-30 lg:h-10  w-full flex flex-col lg:flex-row justify-center items-center gap-6">
      <div class="text-2xl lg:text-md text-gray-500 flex lg:items-center lg:gap-4 flex-col lg:flex-row lg:absolute left-20 bottom-2">
        <strong><i>{{t('Powered-by')}}</i></strong>
        <a href="https://zosiuc.dev" target="_blank">
          <img :src="faceLogo" alt="zosiuc logo" class="lg:h-6">
        </a>
      </div>
      <div class="flex flex-row gap-7 lg:absolute right-20" >
        <a rel="Facebook"
           href="https://www.facebook.com/profile.php?id=61576998966697&__cft__[0]=AZUOQUgLH-NllXVGLhuGpBVf-6JoQbW_sb7iFNrs559L7O7cE1RlIbv5wQaH-_VtAdWGo1GT7BvdF-aalEhk4nh__RjPUfpfyKI_6ohmf6G2RXzF6IhW9rvjQbQHK-d0CixwMAnmieRIVGlBWQtVuVb8BnQK5DrEjIg172fGCELyCA&__tn__=-]K-R"
           target="_blank">
          <img :src="facebook" alt="facebook" class="w-6" />
        </a>
        <a rel="X" href="https://x.com/ZosiucDev" target="_blank">
          <img :src="x" alt="x" class="w-6" />
        </a>
        <a rel="linkedin" href="https://www.linkedin.com/company/zosiuc" target="_blank">
          <img :src="linkedIn" alt="linkedIn" class="w-6"  />
        </a>
        <a rel="whatsapp" href="https://wa.me/31649268880" target="_blank">
          <img :src="whatsapp" alt="linkedIn" class="w-6" />
        </a>
        <a
            rel="email"
            href="mailto:info@zosiuc.dev?subject=Inquiry%20about%20your%20portfolio&body=Hello%2C%0D%0A%0D%0AMy%20name%20is%20[Your%20Name]%2C%20and%20I%20recently%20came%20across%20your%20portfolio.%0D%0A%0D%0AI%20have%20a%20few%20questions%20and%20would%20love%20to%20discuss%20them%20further%20if%20you%20have%20some%20time.%0D%0A%0D%0AThank%20you%20in%20advance%2C%0D%0A%0D%0ABest%20regards%2C%0D%0A[Your%20Name]"
            target="_blank">
          <img :src="email" alt="email" class="w-6" />
        </a>
      </div>
      <div>
        <p class="items-center" >{{t('copyR')}}</p>
      </div>
    </footer>
  </div>
</template>