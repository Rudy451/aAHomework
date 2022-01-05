function scheduleGreatMovieReminder(movie) {
  // remind in one min
  window.setTimeout(function () {
    console.log(`Remember to watch: ${movie}`);
  }, 60 * 1000);
  console.log(`Timer set for ${movie}`);
}

scheduleGreatMovieReminder("Citizen Kane");
scheduleGreatMovieReminder("Touch of Evil");
scheduleGreatMovieReminder("The Third Man");
