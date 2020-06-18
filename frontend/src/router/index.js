import Vue from 'vue'
import VueRouter from 'vue-router';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/edit/:id?',
      name: 'todo-edit',
      component: () => import('../views/TodoEdit')
    },
    {
      path: '/:id',
      name: 'todo-details',
      component: () => import('../views/TodoDetails')
    },
    {
      path: '/',
      name: 'todo-app',
      component: () => import('../views/TodoApp')
    },
  ]
});
