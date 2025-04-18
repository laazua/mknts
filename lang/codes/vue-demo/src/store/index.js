import Vue from 'vue'
import Vuex from 'vuex'
import table from './table'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    table
  }
})