import Vue from 'vue';
import Vuex from 'vuex';

import todoStore from './modules/todoStore';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  modules: {
    todoStore
  }
});
