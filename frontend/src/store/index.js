import Vue from 'vue';
import Vuex from 'vuex';

import todoStore from './modules/todoStore';
import userStore from './modules/userStore';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  modules: {
    todoStore,
    userStore
  }
});
