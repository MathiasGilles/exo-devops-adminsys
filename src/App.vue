<template>
  <amplify-authenticator>
    <div>
      <router-view/>
      <amplify-sign-out></amplify-sign-out>
    </div>
  </amplify-authenticator>
</template>

<script>
export default {
  name: 'App'
}
</script>