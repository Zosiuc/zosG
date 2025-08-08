<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios'


const wait = ref<boolean>(false)
const logoName = ref('')
const data = ref('')
const logo = ref<File | null>(null)
const qrUrl = ref<string | null>(null)
const err = ref<string | null>(null)

function onFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files?.length) {
    const file = target.files[0]
    if (file) {
      logoName.value = file.name
      logo.value = file
    }
  }
}

async function generateQr() {
  wait.value = true
  const formData = new FormData()
  formData.append('data', data.value)
  if (logo.value) formData.append('logo', logo.value)

  try {
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/generate-qr/`, formData, {
      responseType: 'blob',
    })


    qrUrl.value = URL.createObjectURL(response.data)
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response) {
        // Server gaf een fout terug (4xx of 5xx)
        const blob = error.response.data
        const text = await blob.text() // Lees de error als tekst
        console.error('Serverfout:', text)
        err.value = `Fout van server: ${text}`
      } else {
        // Verbindingsfout of iets anders
        console.error('Verbindingsfout of onbekende fout:', error.message)
        err.value = `Verbindingsfout: ${error.message}`
      }
    } else {
      console.error('Onbekende fout:', error)
      err.value = `Er is een onbekende fout opgetreden.`
      alert('Er is een onbekende fout opgetreden.')

    }
  } finally {
    err.value = null
    wait.value = false
  }
}

</script>

<template>
  <div class="">
    <div class="bg-gray-100 min-h-lvh -z-10 absolute top-0 left-0 w-[100vw] flex justify-center items-center">
      <img src="./assets/Icon.svg" alt="logo" class=" blur-xl w-1/2"/>
    </div>

    <div
        class="z-100 max-h-lvh p-6 flex flex-col items-center justify-center   bg-white/25 backdrop-blur-xl">
      <h1 class="text-2xl font-bold mb-4">QR-code Generator</h1>
      <form @submit.prevent="generateQr" class="flex flex-col j gap-10 space-y-4 w-full max-w-sm">
        <input
            type="text"
            v-model="data"
            placeholder="Voer tekst of URL in"
            class="w-full border p-2 rounded"
            required
        />
        <div class="flex flex-col gap-2 bg-blue-100 p-4 rounded-md w-full max-w-sm">
          <label class="text-sm font-medium" for="logo">Optional: Upload your logo to include it in your QR
            code.</label>

          <!-- Verborgen input -->
          <input
              id="logo"
              type="file"
              accept="image/*"
              @change="onFileChange"
              class="hidden"
          />

          <!-- Custom label as button -->
          <label
              for="logo"
              class="cursor-pointer inline-block bg-blue-400 hover:bg-blue-500 text-white text-sm font-semibold py-2 px-4 rounded-md text-center"
          >
            Choose Logo
          </label>

          <!-- Toon bestandsnaam als gekozen -->
          <span v-if="logoName" class="text-sm text-blue-950 truncate">Selected: {{ logoName }}</span>
        </div>


        <button type="submit" class=" bg-blue-400 text-white px-4 py-2 rounded w-full">
          <span v-if="wait">waiting...</span>
          <span v-if="!wait">Genereer QR-code</span>
        </button>
      </form>
    </div>
    <div v-if="err" class=" mt-6 text-red-50 text-center z-100 max-h-lvh p-6 flex flex-col items-center justify-center   bg-white/25 backdrop-blur-xl">
      <strong  v-text="err"></strong>
    </div>

    <div v-if="qrUrl" class=" mt-6 text-center z-100 max-h-lvh p-6 flex flex-col items-center justify-center   bg-white/25 backdrop-blur-xl">
      <h2 class="mb-2 font-semibold">QR-code:</h2>
      <img :src="qrUrl" alt="QR Code" class="border rounded-xl"/>
      <a :href="qrUrl" download="qr-code.png" class="mt-6 inline-block text-gray-600 border p-1 px-3 rounded-2xl">
        Download
      </a>
    </div>
  </div>
</template>


