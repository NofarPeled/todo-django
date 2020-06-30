<template>
  <ul class="todo-list">
    <TodoPreview
      v-for="todo in todos"
      :key="todo._id"
      :todo="todo"
      @onRemoveTodo="onRemoveTodo"
      @onGetTodoById="onGetTodoById"
      @onEditTodo="onEditTodo"
    />
  </ul>
</template>

<script>
import TodoPreview from '@/components/todo/TodoPreview';

export default {
  name: 'todo-list',
  props: {
    todos: Array
  },
  methods: {
    onRemoveTodo(id) {
      this.$emit('removeTodo', id);
    },
    onGetTodoById(id) {
      this.$emit('getTodoById', id);
    },
    onEditTodo(id) {
      this.$emit('editTodo', id);
    }
  },
  components: {
    TodoPreview
  }
};
</script>
