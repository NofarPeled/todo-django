<template>
  <section class="sign-in-section">
    <SignInForm :isSignInMode="isSignInMode" @signIn="signIn" />
    <button
      class="toggle-sign-in-mode"
      @click="toggleIsSignInMode"
    >{{ isSignInMode ? 'Dont have an account ? Sign Up!' : 'Have an account ? Sign In!' }}</button>
  </section>
</template>

<script>
import SignInForm from '@/components/user/SignInForm';

export default {
  data() {
    return {
      isSignInMode: true
    };
  },
  methods: {
    async signIn(user) {
      try {
        await this.$store.dispatch({
          type: this.isSignInMode ? 'signIn' : 'signUp',
          user
        });
        //TODO! PUSH ROUTER!
        //this.$router.push('/');
      } catch (err) {
        //TODO! HANDLE ERROR
        console.log('Got error in user sign in, sign in function: ', err);
      }
    },
    toggleIsSignInMode() {
      this.isSignInMode = !this.isSignInMode;
    }
  },
  components: {
    SignInForm
  }
};
</script>