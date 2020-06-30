<template>
  <div class="todo-details" v-if="todo">
    <nav class="todo-details-nav">
      <router-link class="homepage-link" to="/">HOME</router-link>
      <button class="delete-todo-btn" @click="removeTodo">DELETE</button>
      <router-link class="update-todo-link" :to="`/edit/${todo._id}`">UPDATE</router-link>
    </nav>
    <h2 class="todo-title">{{ todo.title }}</h2>
    <p class="todo-content">{{ todo.content }}</p>
    <h4 class="todo-created-at">{{ todo.created_at }}</h4>
  </div>
</template>

<script>
export default {
  name: 'todo-details',
  async created() {
    const { id } = this.$route.params;
    try {
      await this.$store.dispatch({ type: 'getTodoById', id });
    } catch (err) {
      //TODO: HANDLE THIS ERROR!
      console.log('Got error in created, Todo Details. ', err);
    }
  },
  methods: {
    async removeTodo() {
      //TODO! : CHANGE THIS CONFIRM!
      const confirmedRemove = confirm('are you sure?');
      if (confirmedRemove) {
        try {
          await this.$store.dispatch({ type: 'removeTodo', id: todo._id });
          //TODO! ADD SUCCESS ALERT!
          this.$router.push('/');
        } catch (err) {
          //TODO! HANDLE THIS ERROR!
          console.log('Got error in removeTodo, Todo Details. ', err);
        }
      }
    }
  },
  computed: {
    todo() {
      return this.$store.getters.todo;
    }
  }
};
</script>
