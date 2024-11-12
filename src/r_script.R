path <- "../data/food_data_nutriscore.csv"
data <- read.csv(path)
View(data)

skimr::skim(data)


#Calories
chocolate_bar <- data%>%
  filter(Subcategory=="Pre-made meal")%>%
  pull(Calories)

fast_food <- data%>%
  filter(Subcategory=="Fast food")%>%
  pull(Calories)


plot1 <-  ggplot(data.frame(chocolate_bar),aes(x=chocolate_bar))+
  geom_histogram(aes(y=..density..),binwidth = 60, fill = 'darkgreen',color='white')+
  geom_density(color='orange',size=1)+
  labs(title = "Caloric distribution of pre-made meal",
       x = 'Calories',
       y = 'Frequency')+
  theme_gdocs()

plot2 <-  ggplot(data.frame(fast_food),aes(x=fast_food))+
  geom_histogram(aes(y=..density..),binwidth = 30, fill = 'darkgreen', color='white')+
  geom_density(color='orange',size=1)+
  labs(title = "Caloric distribution of fast food",
       x = 'Calories',
       y = 'Frequency')+
  theme_gdocs()


grid.arrange(plot1,plot2)


#Sugar
palm_oil1 <- data%>%
  filter(Subcategory=="Pre-made meal")%>%
  pull(Palm.oil)

palm_oil2 <- data%>%
  filter(Subcategory=="Fast food")%>%
  pull(Palm.oil)

palm_oil_summary <- data.frame(palm_oil2)%>%
  group_by(palm_oil2)%>%
  summarize(count = n())%>%
  mutate(percentage=count / sum(count) * 100)

palm_oil_summary2 <- data.frame(palm_oil1)%>%
  group_by(palm_oil1)%>%
  summarize(count = n())%>%
  mutate(percentage = count / sum(count) * 100)

ggplot(palm_oil_summary,aes(x="",y=percentage ,fill = factor(test)))+
  geom_bar(stat='identity',width = 1)+
  coord_polar(theta = 'y')+
  labs(title = 'Percentage distribution of palm oil in fast food',
       fill= 'Palm.oil')+
  theme_void()


ggplot(palm_oil_summary2,aes(x="",y=percentage,fill = factor(round(percentage,1))))+
  geom_bar(stat='identity',width = 1, color='white', size=1)+
  coord_polar(theta = 'y')+
  labs(title = 'Percentage distribution of palm oil in fast food\n',
       fill= '')+
  theme_void()+
  geom_text(aes(label = paste0(round(percentage, 1), "%")), 
            position = position_stack(vjust = 0.5), size = 5,color='white',fontface='bold')+
  scale_fill_manual(values = c("lightblue", "deepskyblue"), 
                    labels = c("Without palm oil", "With palm oil"))+
  theme(
    plot.title = element_text(size=17, face = 'bold',hjust=0.5),
    legend.position = 'bottom',
    legend.title = element_text(size=13, face = 'bold'),
    legend.text = element_text(size=11),
    panel.background = element_rect(fill = 'white')
  )
