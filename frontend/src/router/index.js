import Vue from 'vue'
import VueRouter from 'vue-router';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/user/sign-in',
      name: 'user-sign-in',
      component: () => import('../views/user/UserSignIn')
    },
    {
      path: '/edit/:id?',
      name: 'todo-edit',
      component: () => import('../views/todo/TodoEdit')
    },
    {
      path: '/:id',
      name: 'todo-details',
      component: () => import('../views/todo/TodoDetails')
    },
    {
      path: '/',
      name: 'todo-app',
      component: () => import('../views/todo/TodoApp')
    },
  ]
});
