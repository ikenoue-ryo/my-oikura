<template>
  <div>
    <form @input="submit">
				<h2>Contact Info</h2>
				<div class="form-group">
				<label for="Email">Email</label>
				<input type="email" class="form-control" v-model="Email" placeholder="Enter email">
				</div>					
				<div class="form-group">
				<label for="tel">Tel</label>
				<input type="text" class="form-control" v-model="tel" placeholder="Enter phone number">
				</div>
				</form>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'FormName',
    data: () => ({
      Email: null,
      tel: null,
    }),
    methods: {
      submit(){
        this.$emit('update', {
          Email: this.Email,
          tel: this.tel,
        });
      }
    }
  })
</script>
