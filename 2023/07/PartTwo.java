package day7;

import utilities.Input;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class PartTwo {
    private class Hand {
        String hand;
        Map<Character, Integer> handMap;
        int type;

        private Map<Character, Integer> createHandMap(String hand) {
            Map<Character, Integer> handMap = new HashMap<>();
            for (char c : hand.toCharArray()) {
                handMap.put(c, handMap.getOrDefault(c, 0) + 1);
            }
            return handMap;
        }
        public Hand(String hand) {
            this.hand = hand;
            handMap = createHandMap(hand);
            int maxType = 0;
            String[] possibleCards = {"A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4",
                    "3", "2"};
            for (String card : possibleCards) {
                Map<Character, Integer> temp = createHandMap(hand.replace("J", card));
                int currType;
                if (isFiveOfAKind(temp)) currType = 6;
                else if (isFourOfAKind(temp)) currType = 5;
                else if (isFullHouse(temp)) currType = 4;
                else if (isThreeOfAKind(temp)) currType = 3;
                else if (isTwoPair(temp)) currType = 2;
                else if (isOnePair(temp)) currType = 1;
                else currType = 0;
                if (currType > maxType) maxType = currType;
            }
            this.type = maxType;
        }
        public int mapCardToValue(char c) {
            return switch (c) {
                case 'A' -> 14;
                case 'K' -> 13;
                case 'Q' -> 12;
                case 'J' -> 1;
                case 'T' -> 10;
                default -> Character.getNumericValue(c);
            };
        }
        public int compareByCard(Hand other) {
            char[] thisHand = hand.toCharArray();
            char[] otherHand = other.hand.toCharArray();
            for (int i = 0; i < thisHand.length; i++) {
                if (mapCardToValue(thisHand[i]) > mapCardToValue(otherHand[i])) {
                    return 1;
                } else if (mapCardToValue(thisHand[i]) < mapCardToValue(otherHand[i])) {
                    return -1;
                }
            }
            return 0;
        }
        private boolean isFiveOfAKind(Map<Character, Integer> handMap) {
            return handMap.size() == 1;
        }
        private boolean isFourOfAKind(Map<Character, Integer> handMap) {
            return handMap.containsValue(4);
        }
        private boolean isFullHouse(Map<Character, Integer> handMap) {
            return handMap.containsValue(3) && handMap.containsValue(2);
        }
        private boolean isThreeOfAKind(Map<Character, Integer> handMap) {
            return handMap.containsValue(3);
        }
        public boolean isTwoPair(Map<Character, Integer> handMap) {
            ArrayList<Integer> values = new ArrayList<>(handMap.values());
            values.removeIf(value -> value == 2);
            return values.size() == 1;
        }
        private boolean isOnePair(Map<Character, Integer> handMap) {
            return handMap.containsValue(2);
        }

        public int compareTo(Hand other) {
            if (this.type > other.type) return 1;
            else if (this.type < other.type) return -1;
            else return compareByCard(other);
        }
    }

    public static void main(String[] args) {
        PartTwo p1 = new PartTwo();
        String[] input = Input.readInput("day7/input.txt");
        Map<Hand, Integer> bets = new HashMap<>();
        for (String line : input) {
            String[] split = line.split(" ");
            bets.put(p1.new Hand(split[0]), Integer.parseInt(split[1]));
        }
        ArrayList<Hand> ranks = new ArrayList<>(bets.keySet());
        ranks.sort(Hand::compareTo);
        int solution = 0;
        for (int i = 0; i < ranks.size(); i++) {
            System.out.println(ranks.get(i).hand);
            solution += bets.get(ranks.get(i)) * (i+1);
        }
        System.out.println(solution);
    }
}
