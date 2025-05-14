<template>
  <section class="relative h-screen w-screen overflow-hidden scroll-snap-align-start">
    <video autoplay loop muted class="absolute w-auto min-w-full min-h-full max-w-none">
      <source src="../assets/travel_background.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <div class="absolute top-0 left-0 w-full h-full flex items-center justify-center" style="background-color: rgba(0, 0, 0, 0.5);">
      <div class="text-center text-white">
        <h1 class="text-6xl font-bold mb-4">WayfarerAI</h1>
        <p class="text-xl mb-8">Your AI-powered travel companion.</p>
        <button
  @click="$emit('explore')"
  class="bg-transparent border border-black text-black font-bold py-3 px-6 rounded-full absolute bottom-10 left-1/2 transform -translate-x-1/2 transition-all duration-300 ease-in-out hover:bg-white hover:scale-105 hover:shadow-lg flex items-center justify-center"
>
  Explore Destinations
</button>

      </div>
    </div>
  </section>
</template>
