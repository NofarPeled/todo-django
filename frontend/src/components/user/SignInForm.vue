<template>
  <form class="sign-in-form" @submit="onSubmit">
    <h2 class="username_error" v-if="err.username">{{ err.username }}</h2>
    <label for="username" value="User Name" />
    <input type="text" name="username" v-model="user.username" placeholder="Enter User Name" />

    <h2 class="email_error" v-if="err.email">{{ err.email }}</h2>
    <label for="email" value="Email" v-if="!isSignInMode" />
    <input
      type="email"
      name="email"
      v-model="user.email"
      placeholder="Enter Email"
      v-if="!isSignInMode"
    />

    <h2 class="password_error" v-if="err.password">{{ err.password }}</h2>
    <label for="password" value="Password" />
    <input
      type="password"
      name="password"
      v-model="user.password"
      :placeholder="!isSignInMode ? 'Choose Password' : 'Enter Password'"
    />

    <h2 class="re-password_error" v-if="err.re_password">{{ err.re_password }}</h2>
    <label for="re_password" value="Re-Password" v-if="!isSignInMode" />
    <input
      type="password"
      name="re-password"
      v-model="user.re_password"
      placeholder="Re Enter Password"
      v-if="!isSignInMode"
    />

    <input type="submit" :placeholder="isSignInMode ? 'Sign In' : 'Sign Up'" />
  </form>
</template>

<script>
export default {
  props: {
    isSignInMode: Boolean
  },
  data() {
    return {
      user: {},
      err: {}
    };
  },
  methods: {
    onSubmit(ev) {
      ev.preventDefault();
      if (this.user.password !== this.user.re_password && !this.isSignInMode) {
        this.err.password = 'Passwords Must Match!';
        return;
      }
      delete this.user.re_password;
      const userCred = { ...this.user };
      this.$emit('signIn', userCred);
    }
  }
};
</script>