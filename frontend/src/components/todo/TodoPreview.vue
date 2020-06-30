<template>
  <li class="todo-preview">
    <nav class="todo-preview-nav">
      <router-link class="todo-details-link" :to="`/${todo._id}`">DETAILS</router-link>
      <button class="delete-todo-btn" @click="onRemoveTodo">DELETE</button>
      <router-link class="update-todo-link" :to="`/edit/${todo._id}`">UPDATE</router-link>
    </nav>
    <h2 class="title">{{ todo.title }}</h2>
    <p class="description">{{ todo.content }}</p>
    <h4 class="created-at">{{ todo.created_at }}</h4>
  </li>
</template>
<script>
export default {
  name: 'todo-preview',
  props: {
    todo: {
      _id: String,
      title: String,
      content: String,
      completed: Boolean
    }
  },
  methods: {
    onRemoveTodo() {
      this.$emit('onRemoveTodo', this.todo._id);
    }
  }
};
</script>