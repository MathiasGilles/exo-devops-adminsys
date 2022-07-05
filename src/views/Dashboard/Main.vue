<template>
  <div
      style="display: flex; justify-content: center; align-items: center; height: 80%; padding: 3rem; background: darkgrey">
    <button @click="handleClick">Click me</button>
  </div>
</template>

<script>
import {API} from "aws-amplify"

export default {
  methods: {
    handleClick: async () => {
      try {
        await API.post('api001', '/createAnalyse', {})
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>