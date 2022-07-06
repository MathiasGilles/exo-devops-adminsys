import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {
  applyPolyfills,
  defineCustomElements,
} from '@aws-amplify/ui-components/loader';

// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import { Amplify } from 'aws-amplify';
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
import awsExports from './aws-exports';
Amplify.configure(awsExports);

applyPolyfills().then(() => {
  defineCustomElements(window);
});

Vue.config.productionTip = false
Vue.config.ignoredElements = [/amplify-\w*/];

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
