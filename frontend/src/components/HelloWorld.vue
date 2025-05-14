<template>
  <div class="relative min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white flex flex-col items-center justify-center p-6 overflow-hidden">
    <!-- Background Video (optional) -->
    <!--
    <video autoplay loop muted class="absolute top-0 left-0 w-full h-full object-cover opacity-20 z-0">
      <source src="@/assets/travel_background.mp4" type="video/mp4" />
    </video>
    -->

    <div class="relative z-10 text-center">
      <h1 class="text-7xl bg-black font-bold mb-4">GEN AI Assistant</h1>
      <p class="text-xl text-gray-300 mb-8">
        Discover your next adventure with AI-powered travel recommendations.
      </p>
      <button
        @click="$emit('explore')"
        class="px-6 py-3 bg-purple-600 hover:bg-purple-700 rounded-lg text-lg font-semibold transition"
      >
        Start Exploring
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
};
</script>

<style scoped>
/* Add optional scoped styles here */
</style>
