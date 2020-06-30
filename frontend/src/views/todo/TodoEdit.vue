<template>
  <div class="todo-edit">
    <form @submit="onTodoSubmit">
      <label for="todo-title-input" value="Title" />
      <input type="text" name="todo-title-input" placeholder="Enter Title" v-model="todo.title" />

      <label for="todo-content-input" value="Description" />
      <textarea
        type="text"
        name="todo-content-input"
        placeholder="Describe Your Todo"
        v-model="todo.content"
      />

      <label for="todo-completed-checkbox" value="Completed?" />
      <input type="checkbox" name="todo-completed-checkbox" v-model="todo.completed" />

      <input type="submit" placeholder="SUBMIT!" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'todo-edit',
  data() {
    return {
      todo: {
        title: '',
        content: '',
        created_at: '',
        completed: false
      }
    };
  },
  async created() {
    const { id } = this.$route.params;
    if (id) {
      try {
        await this.$store.dispatch({ type: 'getTodoById', id });
        this.todo = { ...this.$store.getters.todo };
      } catch (err) {
        //TODO: HANDLE THIS ERROR!
        console.log('Got error in created, Todo Details. ', err);
      }
    }
  },
  methods: {
    getFormatedDate() {
      const date = new Date();
      return `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).slice(
        -2
      )}-${('0' + date.getDate()).slice(-2)}`;
    },
    async onTodoSubmit(ev) {
      ev.preventDefault();
      try {
        this.todo.created_at = this.todo._id
          ? this.todo.created_at
          : this.getFormatedDate();
        await this.$store.dispatch({
          type: this.todo._id ? 'updateTodo' : 'addTodo',
          todo: { ...this.todo }
        });
      } catch (err) {
        //TODO! HANDLE THIS ERROR!
        console.log('Got error in created, Todo Details. ', err);
      }
    }
  }
};
</script>
