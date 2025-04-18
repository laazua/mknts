import { ref } from 'vue'
import { defineStore  } from "pinia"

export const useAuthStore = defineStore('auth', () => {

  const token = ref(localStorage.getItem('token') || '')

  const setToken = (newToken) => {
    token.value = newToken
    localStorage.setItem('token', token)
  }

  const cleanToken = () => {
    localStorage.removeItem('token')
    token.value = ''
    // localStorage.clear()
  }

  return { token, setToken, cleanToken }
})