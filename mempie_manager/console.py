from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.course import Course
import repositories.course_repository as course_repository

from models.member import Member
import repositories.member_repository as member_repository

course1 = Course("Great British Summer", "8 - 10 August", "10am-3pm", "3 days", "8-12 yrs", "Studio 1", "Ice lollies, Mr Whippy, beach games, water sports... This workshop packs all the best bits of summer into two days of stop motion animation fun!")

course2 = Course("Pixilation Picnic", "11 - 12 August", "10am-3pm", "2 days", "8-12 yrs", "Studio 1", "Animating food is lots of fun (edible props!). At this workshop you will make a picnic as if by magic! We will also be using people as puppets, together with a huge assortment of funny costumes and props, to make pixilation films.")

course3 = Course("Pirates", "19 - 20 September", "10am-3pm", "3 days", "8-12 yrs", "Studio 2", "Ahoy, Matey! Eye patches at the ready! Ye'll have lots o' fun makin' swashbucklin' stop motion animation films. Enjoy a raft of activities to develop skills in 2D and 3D: sailing the high seas, flying fish, sea monsters, walking the plank, a shark attack & more!")

course4 = Course("Halloween", "24 - 26 October", "10am-3pm", "3 days", "8-12 yrs", "Studio 1", "Make spine-tingling stop motion animation films this half-term. Animate creepy cobwebs, scary spiders, bloodcurdling bats, ghastly ghosts and spooky skeletons...if you dare! Mwa haa haa!")

course5 = Course("Weekend Frightfest", "29 - 30 October", "10am-3pm", "2 days", "12-15 yrs", "Studio 2", "Learn gruesome stop motion animation techniques and create chilling films, including a monstrous transformation of a plasticine person into a werewolf!")

course6 = Course("Bonfire Night", "5 -6 November", "10am-3pm", "2 days", "8-12 yrs", "Studio 2", "There will be plenty of 'Oohs' and 'Ahhs!' at this workshop! We will be working some stop motion magic by animating fireworks, sparklers, a bonfire...and more! Learn techniques to make your films an explosion of fun!")

course7 = Course("Festive Fun", "10 - 11 December", "10am-3pm", "2 days", "8-12 yrs", "Studio 1", "Presents, puddings, Father Christmas, feasts, snowflakes, snowballs, snowmen (and more!) will all be putting in an appearance at this jolly holiday workshop.")

member1 = Member("Ray", "Harryhausen", 447488811034, "ray@gmail.com")

member2 = Member("Adam", "Pesapane", 447700184665, "contact@pes.com")

member3 = Member("Henry", "Selick", 447488810936, "skellington@mac.com")

member4 = Member("Tim", "Burton", 447488811033, "tim@frankenweenie.com")

member5 = Member("Nick", "Park", 447700184802, "cheeeeeese@aardman.com")

member6 = Member("Kirsten", "Leopore", 447488810566, "kirstenl@hotmail.com")

booking1 = Booking(member1, course3, "Sophie", "Harryhausen", 9, "None")

booking2 = Booking(member2, course1, "Tom", "Pesapane", 10, "Dyslexia (any written instructions may have to be read out)")

booking3 = Booking(member3, course5, "Jamie", "Selick", 13, "None")

booking4 = Booking(member4, course2, "Eleanor", "Burton", 8, "None")

booking5 = Booking(member4, course2, "George", "Burton", 11, "None")

booking6 = Booking(member5, course4, "Harry", "Park", 11, "None")

booking7 = Booking(member6, course1, "Sally", "Leopore", 9, "None")