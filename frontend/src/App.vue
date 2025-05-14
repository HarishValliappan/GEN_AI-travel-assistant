<template>
  <div class="relative h-screen w-screen bg-gray-900 text-white min-h-screen scroll-snap-type-y mandatory overflow-y-scroll h-screen">
    <Hero @explore="scrollToFeatures" />
    <Features ref="featuresSection" />
    <Footer />
  </div>
</template>

<script>
import Hero from './components/Hero.vue';
import Features from './components/Features.vue';
import Footer from './components/Footer.vue';
import './style.css'

export default {
  name: 'App',
  components: {
    Hero,
    Features,
    Footer,
  },
  methods: {
    scrollToFeatures() {
      this.$refs.featuresSection.$el.scrollIntoView({ behavior: 'smooth' });
    }
  }
};
</script>
