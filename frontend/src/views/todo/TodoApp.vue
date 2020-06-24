<template>
  <div class="todo-app">
    <!-- <TodoFilter />
    <TodoSort />-->
    <TodoList
      v-if="todos"
      :todos="todos"
      @removeTodo="removeTodo"
      @getTodoById="getTodoById"
      @editTodo="editTodo"
    />
  </div>
</template>

<script>
import TodoList from '@/components/todo/TodoList';
// import TodoFilter from '@/components/todo/TodoFilter';
// import TodoSort from '@/components/todo/TodoSort';

export default {
  name: 'todo-app',
  created() {
    try {
      this.$store.dispatch({ type: 'loadTodos' });
    } catch (err) {
      console.log('Got error in TodoApp created. ', err);
    }
  },
  methods: {
    async getTodoById(id) {
      try {
        await this.$store({ type: 'getTodoById', id });
        this.$router.push(`/${id}`);
      } catch (err) {
        console.log('Got error in TodoApp getbyid. ', err);
      }
    },
    async removeTodo(id) {
      try {
        this.$store.dispatch({ type: 'removeTodo', id });
      } catch (err) {
        console.log('Got error in TodoApp temoveTodo. ', err);
      }
    },
    async editTodo(id) {
      this.$store.router.push(`/edit/${id ? id : ''}`);
    }
  },
  computed: {
    todos() {
      return this.$store.getters.todos;
    },
    todo() {
      return this.$store.getters.todo;
    }
  },
  components: {
    TodoList
    // TodoFilter,
    // TodoSort
  }
};
</script>
