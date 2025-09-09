###כרגע דף זה משמש אותי לתיעוד מה אני עושה כל יום בסיום הפרויקט אני אסדר את הקובץ readme###
יום 1
כרגע אני בלמידה


יש לי קריאה של נתיב תיקיית קבצים אניעובר באמצעות סיפרייה קובץ קובץ בתוך התייקיה והיא יודעת לזהות סיומת קבצים גם WAV ואני מייצר לזה את הנתיב המלא לקובץ ספציפי משם אני משתמש בסיפרייה tinytag שמביאה לי metadata על כל קובץ כולל wav

יש לי כמה סוגים ל- kafka שזה כרגע אני לומד כי אני לא התעסקתי עם זה בכלל

יש קצת בלאגן בקוד אני יסדר את זה מחר בבוקר

יום 2
הרצת דוקר
docker pull apache/kafka
docker run -d --name=kafka -p 9092:9092 apache/kafka

kafka
יצרתי קובץ main.py ראשי שעובד
עשיתי גם קובץ main_consumer_test.py
עבור בדיקה לראות שהנתונים מגיעים -kafka
צריך להפעיל קודם את main_consumer_test.py ואז main.py כדי לראות את הנתונים מגיעים לטרמינל של main_consumer_test.py
יש לי קובץ config.py שמכיל את כל ההגדרות של kafka


לגבי מחר אני רוצה לחלק את הכל לצורה של שני סרוויסים שונים שלכל אחד יהיה קובץ config ו- main משלו
התחלתי לעבוד על Elasticsearch ו-mongoDB

יום 3
רק בשביך התיעוד לפני תחילת עבודה בבוקר על אתמול: היה לי צורת kafka מסויימת ובמהלך היום החלטתי לשנות ולקחת מהפרויקט שעשינו בשבוע 11 ניסתי אותו על פרויקט טסט שעשיתי ועשיתי את ההתאמות הנדרות לפרויקט זה ואחרי שזה עבד לקחתי את זה לפה.

הרצת elasticsearch
docker run -d --name es -p 9200:9200 `
 -e "discovery.type=single-node" `
 -e "xpack.security.enabled=false" `
 -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" `
 docker.elastic.co/elasticsearch/elasticsearch:8.15.0

pip install -r requirements.txt מהתקייה של elasticsearch-project

(שומר לעצמי:החיבור עם elasticsearch החזיר אוביקט:
ObjectApiResponse({'name': 'e2b8a91abadf', 'cluster_name': 'docker-cluster', 'cluster_uuid': 'jkZ9x4MdQ6uGFdADF9LMqQ', 'version': {'number': '8.15.0', 'build_flavor': 'default', 'build_type': 'docker', 'build_hash': '1a77947f34deddb41af25e6f0ddb8e830159c179', 'build_date': '2024-08-05T10:05:34.233336849Z', 'build_snapshot': False, 'lucene_version': '9.11.1', 'minimum_wire_compatibility_version': '7.17.0', 'minimum_index_compatibility_version': '7.0.0'}, 'tagline': 'You Know, for Search'})


אוקי אחרי הרבה באלגן כרגע יש לי elasticsearch שכנראה עובד יש איזה EROOR שאני לא מצליח להבין אותו וצריך לדאבג אותו דיברתי עם יניב וכרגע הוא אומר שכדאי שאצא מנקודת הנחה שזה עובד רק צריך עוד לסדר וכרגע המשיך הלאה.
סידרתי לעצמי במחברת תוכנית איך הכל עובד למדתי יותר על השירותים ומי מנהל מה ואני כרגע החלטתי לחלק את זה לשני מכונות
יצירת משימה 2 קובץ לוגים שניתן לנו במשימה שמתי את כל הפרטים אך זה משבש לי את ההפעלה יש מצב שזה בגלל בעיה ב- elasticsearch
אז בגדול אני רוב הזמן עובד עם לוגים ונשאר רק לפתור את הבעיה הזאת ואני ימחק בראש כל מסמך את הסיפריה הרגילה ואני יפעיל את הסיפריה שניתנה
