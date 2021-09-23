<template>
  <div>
    <form @input="submit">
				<h2>Contact Info</h2>
				<div class="form-group">
				<label for="Email">email</label>
				<input type="email" class="form-control" v-model="email" placeholder="Enter email">
				</div>					
				<div class="form-group">
				<label for="tel">Tel</label>
				<input type="text" class="form-control" v-model="tel" placeholder="Enter phone number">
				</div>
				</form>
  </div>
</template>

<script>
  export default {
    name: 'FormContact',
    data() {
      return {
        email: null,
        tel: null,
      }
    },
    methods: {
      submit(){
        this.$emit('update', {
          email: this.email,
          tel: this.tel,
        });
      }
    }
  }
</script>
