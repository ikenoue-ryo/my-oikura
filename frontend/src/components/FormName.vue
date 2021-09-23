<template>
  <div>
    <form @input="submit">
				<h2>Name Info</h2>
				<div class="form-group">
				<label for="first_name">First Name</label>
				<input type="text" class="form-control" v-model="first_name" placeholder="Enter First Name">
				</div>					
				<div class="form-group">
				<label for="last_name">Last Name</label>
				<input type="text" class="form-control" v-model="last_name" placeholder="Enter Last Name">
        </div>
			</form>
  </div>
</template>

<script>
  export default {
    name: 'FormName',
    data() {
      return {
        first_name: null,
        last_name: null,
      }
    },
    methods: {
      submit(){
        this.$emit('update', {
          first_name: this.first_name,
          last_name: this.last_name,
        });
      }
    }
  }
</script>
