<template>
  <div>
    <form @input="submit">
				<h2>User Info</h2>
				<div class="form-group">
				<label for="Birthday">Birthday</label>
				<input type="date" class="form-control" v-model="birthday" placeholder="Enter Birthday">
				</div>
				</form>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'FormName',
    data: () => ({
      birthday: null
    }),
    methods: {
      submit(){
        this.$emit('update', {
          birthday: this.birthday,
        });
      }
    }
  })
</script>
