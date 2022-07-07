<template>
  <div
      style="display: flex; justify-content: center; align-items: center; height: 80%; padding: 3rem; background: darkgrey;flex-direction: column">
    <button @click="handleClick">Create analyse button</button>
    <div style="border: 1px solid black; display: flex; justify-content: space-around">
      <div>id</div>
      <div>title</div>
      <div>description</div>
      <div>transcript</div>
      <div>creation</div>
    </div>
    <div style="border: 1px solid black; display: flex; justify-content: space-around"
         v-for="(items, index) in analyses" :key="index">
      <div><a :href="'/analyses/' + items.id">{{ items.id }}</a></div>
      <div>{{ items.title ?? "Null" }}</div>
      <div>{{ items.description ?? "Null" }}</div>
      <div>{{ items.transcript ?? "Null" }}</div>
      <div>{{ items.created_at }}</div>
    </div>
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
  data: function () {
    return {
      analyses: [],
      analysesKey: []
    }
  },
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
        return await API.get('api001', '/getAnalyses')
      } catch (e) {
        console.log(e)
      }
    }
  },
  mounted: async function () {
    this.analyses = await this.fetchAnalysis()
    this.analysesKey = Object.keys(this.analyses[0])
  }
}
</script>