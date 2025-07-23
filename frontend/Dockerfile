FROM node:18

WORKDIR /app

# Устанавливаем зависимости
COPY package*.json ./
RUN npm install

# Копируем остальные файлы
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]