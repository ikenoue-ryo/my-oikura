module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  outputDir: '../staticfiles',
  indexPath: '../templates/index.html',
  publicPath: process.env.NODE_ENV === 'production'
    ? '/staticfiles/'
    : '/'
}
