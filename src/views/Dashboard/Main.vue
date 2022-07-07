<template>
  <div
      style="display: flex; justify-content: center; align-items: center; height: 80%; padding: 3rem; background: darkgrey;flex-direction: column">
    <button @click="handleClick">Create analyse button</button>
    <div style="display: flex;gap: 20px;">
      <p>Mathias GILLES</p>
      <p>Jules DAYAUX</p>
      <p>Sosthène FRUCHARD</p>
      <p>Yanny OUZID</p>
    </div>
  </div>
</template>

<script>
import {API} from "aws-amplify"

export default {
  methods: {
    handleClick: async () => {
      try {
        await API.post('api001', '/createAnalyse')
      } catch (e) {
        console.log(e);
      }
    },
    fetchAnalysis: async () => {
      try {
        const response = await API.get('api001', '/getAnalyses')
        console.log(response);
      } catch (e) {
        console.log(e)
      }
    }
  },
  mounted: async function () {
    await this.fetchAnalysis()
  }
}
</script>