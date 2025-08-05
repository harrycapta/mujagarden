#!/bin/bash
# Script per copiare il digital garden in /var/www/garden.mujarrib.com (usato da Caddy)

DEST=/var/www/garden.mujarrib.com

echo "📦 Deploying to $DEST ..."
mkdir -p $DEST/posts
cp index.html style.css $DEST/
cp posts/* $DEST/posts/
echo "✅ Deploy complete!"
