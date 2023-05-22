module.exports = {
  branches: [
    'master', // replace with your default branch name
    { name: 'develop', prerelease: true, channel: 'develop' },
  ], 
  plugins: [
    [
      '@semantic-release/commit-analyzer',
      {
        releaseRules: [
          { type: 'bug', release: 'patch' },
          { type: 'fix', release: 'patch' },
          { type: 'feature', release: 'minor' },
          { type: 'break', release: 'major' },
        ],
      },
    ],
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    '@semantic-release/npm',
    [
      '@semantic-release/git',
      {
        assets: ['package.json', 'yarn.lock', 'CHANGELOG.md'],
        message:
          'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
      },
    ],
    '@semantic-release/github',
  ],
};
