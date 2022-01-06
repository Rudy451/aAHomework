var path = require('path');

module.exports = {
  entry: {
    app: ['./app/app.jsx'],
  },
  output: {
    path: path.resolve(__dirname, 'app'),
    filename: 'bundle.js'
  },
  module: {
    rules: [{
      loader: 'babel-loader',
      options: {presets: ["@babel/env"]}
  }]
  },
  resolve: {
    extensions: ['.js', '.jsx', '*']
  },
  devtool: 'hidden-source-map'
}
